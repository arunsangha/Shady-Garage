# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-03-13 22:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meets', '0006_auto_20180228_1614'),
    ]

    operations = [
        migrations.AddField(
            model_name='meet',
            name='marker_image',
            field=models.ImageField(choices=[('BMW E30', 'static/images/e30marker.svg'), ('MARKER SVG', 'static/images/marker.svg')], default='BMW E30', upload_to=''),
        ),
    ]
