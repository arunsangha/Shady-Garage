from django.db import models
from products.models import ProductItem
from django.contrib.auth import get_user_model
User = get_user_model()
from django.db.models.signals import m2m_changed, pre_save


class CartManager(models.Manager):
    def new(self, user=None):
        user_obj = None
        if user is not None:
            if user.is_authenticated():
                user_obj = user
        return self.model.objects.create(user=user_obj)

    def get_or_create(self, request):
        cart_id = request.session.get('cart_id')
        qs = self.get_queryset().filter(id=cart_id)

        if qs.count() == 1:
            cart_obj = qs.first()
            new_obj = False
            if request.user.is_authenticated() and cart_obj.user is None:
                cart_obj.user = request.user
                cart_obj.save()

        else:
            cart_obj = Cart.objects.new(user=request.user)
            new_obj = True
            request.session['cart_id'] = cart_obj.id

        return cart_obj, new_obj


class Cart(models.Model):
    user            = models.ForeignKey(User, related_name="carts_user_fk", blank=True, null=True)
    products        = models.ManyToManyField(ProductItem, related_name="products_in_cart", blank=True)
    sub_total       = models.DecimalField(default=0, max_digits=20, decimal_places=2)
    total           = models.DecimalField(default=0, max_digits=20, decimal_places=2)
    shipping        = models.PositiveIntegerField(default=0)
    active          = models.BooleanField(default=True)
    update          = models.DateTimeField(auto_now_add=True)
    timestamp       = models.DateTimeField(auto_now_add=True)

    objects         = CartManager()

    def set_inactive(self):
        self.active = False
        self.save()
        return self.active

    def update_prices(self):
        updated = False
        price = self.total
        total = 0
        for x in self.products.all():
            if x.product_size_fk.product_fk.sale == True:
                total += (x.product_size_fk.product_fk.sale_price * x.quantity)
            else:
                total += (x.product_size_fk.product_fk.price * x.quantity)

        print("Price:" + str(price))
        print(total)
        if total != price:
            self.sub_total = total
            self.save()
            updated = True
        return updated

    def __str__(self):
        return "{}-Products Count:{}".format(self.id, self.products.count())



#Update products (ManyToManyField) in Cart and updates the sub_total and total price
def m2m_changed_cart_receiver(sender, instance, action, *args, **kwargs):
    if action == 'post_add' or action == 'post_remove' or action == 'post_clear':
        products_qs = instance.products.all()
        total = 0

        for product in products_qs:
            if product.product_size_fk.product_fk.sale == True:
                total += (product.product_size_fk.product_fk.sale_price * product.quantity)
            else:
                total += (product.product_size_fk.product_fk.price * product.quantity)

        print(total)
        if instance.sub_total != total:
            instance.sub_total = total
            instance.save()

m2m_changed.connect(m2m_changed_cart_receiver, sender=Cart.products.through)


def pre_save_cart_receiver(sender, instance, *args, **kwargs):



    if float(instance.sub_total) < 300:
        instance.shipping = 40
        total = float(instance.sub_total) + instance.shipping
    else:
        instance.shipping = 0
    total = float(instance.sub_total)
    instance.total = total + instance.shipping

pre_save.connect(pre_save_cart_receiver, sender=Cart)
