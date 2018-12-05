# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-12-05 02:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_post_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='has_blurred_thumbnail',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='thumbnail_blurred',
            field=models.ImageField(blank=True, null=True, upload_to='thumbnail_blurred'),
        ),
    ]
