# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-08 19:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('podcast', '0003_auto_20160808_1927'),
    ]

    operations = [
        migrations.AddField(
            model_name='episode',
            name='slug',
            field=models.SlugField(default='bum'),
            preserve_default=False,
        ),
    ]
