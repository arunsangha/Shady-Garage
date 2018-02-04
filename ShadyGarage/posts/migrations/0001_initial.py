# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-29 23:16
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_title', models.CharField(max_length=100)),
                ('post_image', models.ImageField(blank=True, upload_to='post_pic')),
                ('post_description', models.TextField(blank=True, max_length=255)),
                ('slug', models.SlugField(unique=True)),
                ('post_likes', models.ManyToManyField(blank=True, related_name='post_likes', to=settings.AUTH_USER_MODEL)),
                ('user_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_posting', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]