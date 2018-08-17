from django.db import models
from addresses.models import Address
from billing.models import BillingProfile
from carts.models import Cart
from django.contrib.auth import get_user_model
from django.db.models.signals import pre_save, post_save
from ShadyGarage.utils import unique_order_id_generator

User = get_user_model()


ORDER_STATUS = (
    ('created', 'Opprettet'),
    ('paid', 'Betal'),
    ('packing', 'Pakker'),
    ('shippped', 'Sendt'),
    ('finished', 'Finished'),
)
class Order(models.Model):
    order_id            = models.CharField(max_length=120, unique=True, blank=True)
    user                = models.ForeignKey(User, related_name="order_user")
    cart                = models.ForeignKey(Cart, related_name="order_cart")
    billing_profile     = models.ForeignKey(BillingProfile, related_name="order_billing_profile")
    shipping_address    = models.ForeignKey(Address, related_name="order_shipping_address")
    billing_address     = models.ForeignKey(Address, related_name="order_billing_profile")
    status              = models.CharField(choices=ORDER_STATUS, default='created', max_length=120)
    total               = models.DecimalField(default=0, max_digits=1000, decimal_places=2)
    timestamp           = models.DateTimeField(auto_now_add=True)
    active              = models.BooleanField(default=True)

    def __str__(self):
        return self.order_id

    def update_total(self):
        self.total = self.cart.total_price
        self.save()
        return total

    def check_done(self):
        billing_profile = self.billing_profile
        shipping_address = self.shipping_address
        billing_address = self.billing_address
        total = self.total

        if billing_profile and shipping_address and billing_address and total:
            return True
        return False

    def set_paid(self):
        if self.check_done():
            self.status = 'paid'
            self.save()
        return self.status

def pre_save_create_order(sender, instance, *args, **kwargs):
    if not instance.order_id:
        instance.order_id = unique_order_id_generator()

    #Check if a order with same cart exists. If so, deactivate it
    qs = Order.objects.filter(cart=instance.cart).exlude(billing_profile=instance.billing_profile)

    if qs.exists():
        qs.update(active=False)

pre_save.connect(pre_save_create_order, sender=Order)

#?? From udemy...
def post_save_cart_total(sender, instance, *args, **kwargs):
    if not created:
        cart_obj = instance
        cart_total = instance.total
        cart_id = instance.id
        qs = Order.objects.filter(cart__id=cart_id)
        if qs.count() == 1:
            order_obj = qs.first()
            order_obj.update_total()

post_save.connect(post_save_cart_total, sender=Cart)

def post_save_order(sender, instance, *args, **kwargs):
    if created:
        instance.update_total()
post_save.connect(post_save_order, sender=Order)