# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-21 12:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('podcast', '0005_auto_20160813_1355'),
    ]

    operations = [
        migrations.CreateModel(
            name='Podcast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=140)),
                ('link', models.CharField(max_length=140)),
                ('author_name', models.CharField(max_length=140)),
                ('description', models.TextField()),
                ('summary', models.CharField(max_length=140)),
                ('iTunes_name', models.CharField(max_length=140)),
                ('iTunes_email', models.CharField(max_length=140)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
