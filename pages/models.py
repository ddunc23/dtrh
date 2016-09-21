from __future__ import unicode_literals

from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class Page(models.Model):
	title = models.CharField(max_length=128)
	slug = models.SlugField()
	body = RichTextUploadingField(blank=True)

	def __unicode__(self):
		return self.title