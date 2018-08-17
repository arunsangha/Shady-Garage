from django.db import models
from django.utils.text import slugify
# Create your models here.

class Product(models.Model):
    CATEGORY_CHOICES = (("STICKER", "Sticker"), ("Hoodie", "Hoodie"), ("TSHIRT", "Tshirt"))

    name            = models.CharField(max_length=100)
    description     = models.TextField(max_length=255)
    category        = models.CharField(choices=CATEGORY_CHOICES, max_length=50, default="Sticker")
    price           = models.PositiveIntegerField()
    stock           = models.PositiveIntegerField()
    empty           = models.BooleanField(default=False)
    slug            = models.SlugField(allow_unicode=True, unique=True)
    timestamp       = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def is_empty(self):
        if stock == 0:
            self.empty = True
        return self.empty

    def get_price(self):
        return self.price

    def get_stock(self):
        return get_stock

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save()

class ProductImage(models.Model):
    product_fk     = models.ForeignKey(Product, related_name="product_image")
    image          = models.ImageField(upload_to="shady_shop")
