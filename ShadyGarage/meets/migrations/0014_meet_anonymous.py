# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-05-29 13:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meets', '0013_auto_20180527_1621'),
    ]

    operations = [
        migrations.AddField(
            model_name='meet',
            name='anonymous',
            field=models.BooleanField(default=False),
        ),
    ]
