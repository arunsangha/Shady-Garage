# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-11-13 21:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20180906_1903'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(blank=True, default=1, null=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductSize',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'XL'), ('XXL', 'XXL'), ('One Size', 'One Size')], max_length=10)),
                ('quantity', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('empty', models.BooleanField(default=False)),
                ('product_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products_fk_size', to='products.Product')),
            ],
        ),
        migrations.AddField(
            model_name='productitem',
            name='product_size_fk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_size_fk', to='products.ProductSize'),
        ),
    ]
