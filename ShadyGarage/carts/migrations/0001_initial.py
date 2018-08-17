# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-08-17 18:43
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0002_auto_20180817_0124'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_total', models.PositiveIntegerField()),
                ('total', models.PositiveIntegerField()),
                ('shipping', models.PositiveIntegerField()),
                ('active', models.BooleanField(default=True)),
                ('update', models.DateTimeField(auto_now_add=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('products', models.ManyToManyField(related_name='products_in_cart', to='products.Product')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='carts_user_fk', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
