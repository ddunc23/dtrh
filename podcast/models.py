from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from taggit.managers import TaggableManager
from datetime import datetime

def podcast_directory_path(instance, filename):
	"""Function to ensure podcast files will be uploaded to /uploads/podcasts/date/filename""" 

	return 'uploads/podcasts/{0}/{1}'.format(instance.date_broadcast, filename)


class Episode(models.Model):
	"""An Epsiode of the DTRH podcast and associated gubbins"""
	title = models.CharField(max_length=128)
	slug = models.SlugField()
	file = models.FileField(upload_to=podcast_directory_path, null=False, blank=False, verbose_name='Audio File')
	created = models.DateField(auto_now_add=True, null=True, blank=True)
	date_broadcast = models.DateTimeField(null=True, blank=False)
	published = models.BooleanField(default=False)
	body = RichTextUploadingField(blank=False)
	tags = TaggableManager(blank=True)
	description = models.TextField(null=False, blank=False)

	def __unicode__(self):
		return str(self.date_broadcast) + ' | ' + self.title

	def get_absolute_url(self):
		return reverse('podcast-episode', args=[str(self.date_broadcast.year), str(self.date_broadcast.month), str(self.slug)])