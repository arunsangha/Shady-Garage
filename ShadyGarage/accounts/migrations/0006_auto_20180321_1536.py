# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-21 14:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20180321_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='thumbnail',
            field=models.ImageField(default='default/default.png', upload_to='profile_pic_thumbnail'),
        ),
    ]
