# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-09-06 19:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20180906_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customproduct',
            name='description',
            field=models.TextField(),
        ),
    ]