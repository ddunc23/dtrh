# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-08 19:05
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
    ]

    operations = [
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('created', models.DateField(auto_now_add=True, null=True)),
                ('published', models.BooleanField(default=False)),
                ('body', ckeditor_uploader.fields.RichTextUploadingField()),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
        ),
    ]
