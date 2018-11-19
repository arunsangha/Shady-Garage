from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Product)
admin.site.register(models.ProductImage)
admin.site.register(models.ProductSize)
admin.site.register(models.ProductItem)
admin.site.register(models.CustomProduct)
