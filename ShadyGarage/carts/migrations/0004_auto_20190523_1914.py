# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2019-05-23 19:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0003_auto_20180823_0206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(blank=True, related_name='products_in_cart', to='products.ProductItem'),
        ),
    ]
