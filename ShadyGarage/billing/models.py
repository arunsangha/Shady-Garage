from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import pre_save, post_save
from django.conf import settings

import stripe
stripe.api_key = getattr(settings, "STRIPE_API_KEY", "sk_test_czI0R33pVrj3VrDfBg1xbSSN")
User = get_user_model()

class BillingProfileManager(models.Manager):
    def new_or_get(self, request):
        user = request.user
        created = False
        billing_profile = None

        if user.is_authenticated():
            billing_profile, created = self.model.objects.get_or_create(user=user, email=user.email)

        return billing_profile, created

class BillingProfile(models.Model):
    user             = models.OneToOneField(User, related_name="billing_profile_user")
    email            = models.EmailField()
    active           = models.BooleanField(default=True)
    timestamp        = models.DateTimeField(auto_now_add=True)
    #Strippe customer id
    customer_id      = models.CharField(max_length=120, null=True, blank=True)

    objects = BillingProfileManager()
#Creates a stripe customer and adds stripe customer id to profile.
#This happens before the billing profile objects get saved.
def billing_profile_created_recevier(sender, instance, *args, **kwargs):
    if not instance.customer_id and instance.email:
        customer = stripe.Customer.create(
            email = instance.email
        )

        instance.customer_id = customer.id

pre_save.connect(billing_profile_created_recevier, sender=BillingProfile)

#When a user is created, the billingprofile for the user will also be created
def user_created_recevier(sender, created, instance, *args, **kwargs):
    if created and instance.email:
        BillingProfile.objects.get_or_create(user=instance, email=instance.email)

post_save.connect(user_created_recevier, sender=User)
