# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-02-28 15:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meets', '0005_auto_20180227_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meet',
            name='location',
            field=models.CharField(max_length=1275),
        ),
    ]
