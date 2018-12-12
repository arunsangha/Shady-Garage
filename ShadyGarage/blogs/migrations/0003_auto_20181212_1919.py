# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-12-12 19:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_blog_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=20)),
                ('model', models.CharField(max_length=20)),
                ('price', models.CharField(max_length=40)),
                ('engine', models.CharField(max_length=50)),
                ('zero_to_100', models.DecimalField(decimal_places=2, max_digits=5)),
                ('consumption', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.RemoveField(
            model_name='blog',
            name='consumption',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='engine',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='price',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='zero_to_100',
        ),
        migrations.AddField(
            model_name='blog',
            name='car',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='car_fk', to='blogs.Car'),
            preserve_default=False,
        ),
    ]
