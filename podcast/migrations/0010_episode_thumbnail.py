# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-25 12:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('podcast', '0009_episode_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='episode',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/%Y/%m/%d/'),
        ),
    ]
