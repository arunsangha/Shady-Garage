# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-14 22:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meets', '0008_auto_20180314_2313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meet',
            name='marker_image',
            field=models.CharField(choices=[('static/images/e30marker.svg', 'BMW E30'), ('static/images/Stance.svg', 'Audi A4 B8 Stance'), ('static/images/lamborghini.svg', 'Lamborghini Huracan')], default='static/images/e30marker.svg', max_length=255),
        ),
    ]
