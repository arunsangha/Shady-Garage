# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-09 21:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_remove_notification_profile_pic_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(blank=True, upload_to='thumbnail'),
        ),
    ]
