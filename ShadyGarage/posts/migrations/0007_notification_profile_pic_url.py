# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-08 21:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_notification_noti_reply_fk'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='profile_pic_url',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
