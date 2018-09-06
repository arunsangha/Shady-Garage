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

class CustomProduct(models.Model):
    user        = models.ForeignKey(User, related_name="custom_product_user")
    mobile      = models.CharField(max_length=25)
    description = models.CharField(max_length=240)
    image       = models.ImageField(upload_to="custom_product")
