# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-09-06 15:22
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0006_remove_product_size'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.CharField(max_length=25)),
                ('description', models.CharField(max_length=240)),
                ('image', models.ImageField(upload_to='custom_product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='custom_product_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
