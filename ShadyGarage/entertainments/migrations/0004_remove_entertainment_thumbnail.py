# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-06-24 19:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entertainments', '0003_entertainment_thumbnail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entertainment',
            name='thumbnail',
        ),
    ]
