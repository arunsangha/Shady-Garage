# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-08-17 01:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='shady_shop')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('STICKER', 'Sticker'), ('Hoodie', 'Hoodie'), ('TSHIRT', 'Tshirt')], default='Sticker', max_length=50),
        ),
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(allow_unicode=True, default=4141421, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productimage',
            name='product_fk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_image', to='products.Product'),
        ),
    ]