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
    #Stripe customer id
    customer_id      = models.CharField(max_length=120, null=True, blank=True)

    objects = BillingProfileManager()


    def __str__(self):
        return self.user.username

    def charge(self, order_obj, card=None):
        return Charge.objects.create(self, order_obj, card)

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


class CardManager(models.Manager):
    #Return all cards that are active
    def all(self, *args, **kwargs):
        return self.get_queryset().filter(active=True)

    def add_new(self, billing_profile, token):
        if token:
            customer = stripe.Customer.retrieve(billing_profile.customer_id)
            stripe_card_response = customer.sources.create(source=token)
            new_card = self.model(
                billing_profile = billing_profile,
                stripe_id = stripe_card_response.id,
                brand = stripe_card_response.brand,
                country = stripe_card_response.country,
                exp_month = stripe_card_response.exp_month,
                exp_year = stripe_card_response.exp_year,
                last4 = stripe_card_response.last4,
            )

            new_card.save()
            return new_card

        return None


class Card(models.Model):
    billing_profile    = models.ForeignKey(BillingProfile, related_name="card_billing_profile")
    stripe_id          = models.CharField(max_length=120)
    brand              = models.CharField(max_length=120, null=True, blank=True)
    country            = models.CharField(max_length=120, null=True, blank=True)
    exp_month          = models.IntegerField(blank=True, null=True)
    exp_year           = models.IntegerField(blank=True, null=True)
    last4              = models.CharField(max_length=4, blank=True, null=True)
    default            = models.BooleanField(default=True)
    active             = models.BooleanField(default=True)
    timestamp          = models.DateTimeField(auto_now_add=True)

    objects = CardManager()



    def __str__(self):
        return self.last4

#Creates the charge with stripe add creates charge object
class ChargeManager(models.Manager):
    def create(self, billing_profile, order_obj, card=None):
        card_obj = card
        if card_obj is None:
            cards = billing_profile.card_set.filter(default=True)
            if cards.exists():
                card_obj = cards.first()

        if card_obj is None:
            return False, "No card available"

        c = stripe.Charge.create(
            amount = int(order_obj.total * 100),
            currency = "nok",
            customer = billing_profile.customer_id,
            source = card_obj.stripe_id,
            metadata = {'order_id':order_obj.order_id}
        )


        new_charge_obj = self.model(
            billing_profile = billing_profile,
            stripe_id = c.id,
            paid  = c.paid,
            refunded = c.refunded,
            outcome = c.outcome,
            outcome_type = c.outcome['type'],
            seller_message = c.outcome.get('seller_message'),
            risk_level = c.outcome.get('risk_level'),
        )

        new_charge_obj.save()

        return new_charge_obj.paid, new_charge_obj.seller_message

class Charge(models.Model):
    billing_profile     = models.ForeignKey(BillingProfile, related_name="charge_billing_profile")
    stripe_id           = models.CharField(max_length=120)
    paid                = models.BooleanField(default=False)
    refunded            = models.BooleanField(default=False)
    outcome             = models.TextField(blank=True, null=True)
    outcome_type        = models.CharField(max_length=120, null=True, blank=True)
    seller_message      = models.CharField(max_length=120, null=True, blank=True)
    risk_level          = models.CharField(max_length=120, null=True, blank=True)


    objects = ChargeManager()

    def __str__(self):
        return self.stripe_id
