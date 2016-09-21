from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from taggit.managers import TaggableManager
from datetime import datetime
from filebrowser.fields import FileBrowseField

def podcast_directory_path(instance, filename):
	"""Function to ensure podcast files will be uploaded to /uploads/podcasts/date/filename""" 

	return 'uploads/podcasts/{0}/{1}'.format(instance.date_broadcast, filename)


class SingletonModel(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.__class__.objects.exclude(id=self.id).delete()
        super(SingletonModel, self).save(*args, **kwargs)

    @classmethod
    def load(cls):
        try:
            return cls.objects.get()
        except cls.DoesNotExist:
            return cls()


class Podcast(SingletonModel):
	"""Global settings for the DTRH podcast"""
	title = models.CharField(max_length=140)
	link = models.CharField(max_length=140)
	author_name = models.CharField(max_length=140)
	description = models.TextField()
	summary = models.CharField(max_length=140)
	iTunes_name = models.CharField(max_length=140)
	iTunes_email = models.CharField(max_length=140)

	class Meta:
		verbose_name = 'Podcast Settings'
		verbose_name_plural = 'Podcast Settings'

	def __unicode__(self):
		return self.title


class Episode(models.Model):
	"""An Epsiode of the DTRH podcast and associated gubbins"""
	title = models.CharField(max_length=128)
	slug = models.SlugField()
	#file = models.FileField(upload_to=podcast_directory_path, null=True, blank=False, verbose_name='Audio File')
	file = FileBrowseField('Audio', max_length=200, directory='uploads/', extensions=['.mp3'], blank=True, null=True)
	created = models.DateField(auto_now_add=True, null=True, blank=True)
	date_broadcast = models.DateTimeField(null=True, blank=False)
	published = models.BooleanField(default=False)
	body = RichTextUploadingField(blank=False)
	tags = TaggableManager(blank=True)
	description = models.TextField(null=False, blank=False)

	def __unicode__(self):
		# return str(self.date_broadcast.date.strftime('%d %M %y') + ' | ' + self.title)
		return self.date_broadcast.strftime('%d %B %Y') + ' | ' + self.title

	def get_absolute_url(self):
		return reverse('podcast-episode', args=[str(self.date_broadcast.year), str(self.date_broadcast.month), str(self.slug)])