# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-12-12 19:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_auto_20181212_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='consumption',
            field=models.DecimalField(decimal_places=1, max_digits=5),
        ),
        migrations.AlterField(
            model_name='car',
            name='zero_to_100',
            field=models.DecimalField(decimal_places=1, max_digits=5),
        ),
    ]
