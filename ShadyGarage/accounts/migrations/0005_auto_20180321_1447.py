# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-21 13:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20180320_2338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(default='default/default.png', upload_to='profile_pic'),
        ),
    ]
