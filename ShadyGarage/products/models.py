from django.db import models
from django.utils.text import slugify
from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.

class Product(models.Model):
    CATEGORY_CHOICES = (("STICKER", "Sticker"), ("Hoodie", "Hoodie"), ("TSHIRT", "Tshirt"))
    name            = models.CharField(max_length=100)
    description     = models.TextField(max_length=255)
    category        = models.CharField(choices=CATEGORY_CHOICES, max_length=50, default="Sticker")
    price           = models.DecimalField(decimal_places=2, max_digits=30)
    stock           = models.PositiveIntegerField()
    empty           = models.BooleanField(default=False)
    slug            = models.SlugField(allow_unicode=True, unique=True)
    timestamp       = models.DateTimeField(auto_now_add=True)
    sale            = models.BooleanField(default=False)
    sale_price      = models.DecimalField(decimal_places=2, max_digits=30, blank=True, null=True)
    sale_percentage = models.PositiveIntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return self.name

    def is_empty(self):
        if self.stock == 0:
            self.empty = True
        return self.empty

    def get_price(self):
        return self.price

    def get_stock(self):
        return self.stock

    def get_list_image(self):
        qs = self.product_image.all()
        if qs.exists():
            print(qs.first())
            image = qs.first()
            return image.image.url
        return None

    def get_absolute_url(self, *args, **kwargs):
        return reverse("products:detail", kwargs={'category':'sticker', 'slug':self.slug})

    def take_one(self):
        success = False
        if self.stock > 0:
            self.stock = self.stock - 1
            success = True
        else:
            self.empty = True
        self.save()
        return success

    def has_size(self):
        has_ = False
        if self.category == "TSHIRT":
            has_ = True
        return has_

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save()

class ProductImage(models.Model):
    product_fk     = models.ForeignKey(Product, related_name="product_image")
    image          = models.ImageField(upload_to="shady_shop")

    def __str__(self):
        return self.product_fk.name


PRODUCT_SIZE = (
    ('S', 'Small'),
    ('M', 'Medium'),
    ('L', 'Large'),
    ('XL', 'XL'),
    ('XXL', 'XXL'),
    ('OneSize', 'OneSize'),
)
class ProductSize(models.Model):
    product_fk    = models.ForeignKey(Product, related_name="products_fk_size")
    size          = models.CharField(max_length=10, choices=PRODUCT_SIZE)
    quantity      = models.PositiveIntegerField(default=0, blank=True, null=True)
    empty         = models.BooleanField(default=False)

    def __str__(self):
        return "{}-{}".format(self.product_fk.name, self.size)

    def is_empty(self):
        empty = False
        if self.quantity == 0:
            self.empty = True
            empty = True
        return empty



    def take_one(self):
        success = False
        if (self.quantity > 0) and self.is_empty() == False:
            self.quantity = self.quantity - 1
            success = True
        return success


class ProductItem(models.Model):
    cart_id           = models.PositiveIntegerField(default=1)
    product_size_fk   = models.ForeignKey(ProductSize, related_name="product_cart_size_fk")
    quantity          = models.PositiveIntegerField(default=1, blank=True, null=True)
    active            = models.BooleanField(default=True)

    def take_one(self):
        success = False
        product_quantity = self.product_size_fk.quantity
        to_take = self.quantity
        if product_quantity > to_take:
            self.product_size_fk.quantity = self.product_size_fk.quantity - to_take
            self.product_size_fk.save()
            success = True
        return success

    def __str__(self):
        return "{}".format(self.cart_id)

class CustomProduct(models.Model):
    user              = models.ForeignKey(User, related_name="custom_product_user")
    mobile            = models.CharField(max_length=25)
    instagram_profile = models.CharField(max_length=100, blank=True, null=True)
    facebook_profile  = models.CharField(max_length=200, blank=True, null=True)
    description       = models.TextField()
    image             = models.ImageField(upload_to="custom_product", blank=True, null=True)

    def __str__(self):
        return self.user.username
