# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-31 18:49
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(max_length=1020)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-post_created']},
        ),
        migrations.AddField(
            model_name='post',
            name='post_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='postcomment',
            name='post_fk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_comment_fk', to='posts.Post'),
        ),
        migrations.AddField(
            model_name='postcomment',
            name='user_fk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_comment_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
