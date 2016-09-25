# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-25 12:28
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('podcast', '0008_auto_20160921_1348'),
    ]

    operations = [
        migrations.AddField(
            model_name='episode',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
