from django.shortcuts import render, get_object_or_404
from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Rss201rev2Feed
from models import Episode, Podcast
import datetime
from mutagen.mp3 import MP3
import os
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



def post_list(request):
	episodes = Episode.objects.filter(file='', date_broadcast__date__lte=datetime.date.today()).order_by('-date_broadcast')
	paginator = Paginator(episodes, 10)

	page = request.GET.get('page')
	
	try:
		episodes = paginator.page(page)
	except PageNotAnInteger:
		episodes = paginator.page(1)
	except EmptyPage:
		episodes = paginator.page(paginator.num_pages)

	return render(request, 'podcast/post_list.html', {'episodes': episodes})


def post(request, year, month, slug):
	post = get_object_or_404(Episode, slug=slug, date_broadcast__year=year, date_broadcast__month=month)

	return render(request, 'podcast/post.html', {'post': post})	


def posts_by_year(request, year):
	episodes = Episode.objects.filter(file='', date_broadcast__lte=datetime.date.today(), date_broadcast__year=year).order_by('-date_broadcast')
	paginator = Paginator(episodes, 10)

	page = request.GET.get('page')
	
	try:
		episodes = paginator.page(page)
	except PageNotAnInteger:
		episodes = paginator.page(1)
	except EmptyPage:
		episodes = paginator.page(paginator.num_pages)

	return render(request, 'podcast/post_list.html', {'episodes': episodes})



def episode_list(request):
	episodes = Episode.objects.exclude(file='').order_by('-date_broadcast')
	#paginator = Paginator(episodes, 10)

	#page = request.GET.get('page')
	
	#try:
	#	episodes = paginator.page(page)
	#except PageNotAnInteger:
	#	episodes = paginator.page(1)
	#except EmptyPage:
	#	episodes = paginator.page(paginator.num_pages)

	return render(request, 'podcast/episode_list.html', {'episodes': episodes})


def episode(request, year, month, slug):
	episode = get_object_or_404(Episode, slug=slug, date_broadcast__year=year, date_broadcast__month=month)

	return render(request, 'podcast/episode.html', {'episode': episode})



class iTunesPodcastsFeedGenerator(Rss201rev2Feed):

	def rss_attributes(self):
		return {u"version": self._version, u"xmlns:atom": u"http://www.w3.org/2005/Atom", u'xmlns:itunes': u'http://www.itunes.com/dtds/podcast-1.0.dtd'}

	def add_root_elements(self, handler):
		super(iTunesPodcastsFeedGenerator, self).add_root_elements(handler)
		handler.addQuickElement(u'itunes:subtitle', self.feed['subtitle'])
		handler.addQuickElement(u'itunes:author', self.feed['author_name'])
		handler.addQuickElement(u'itunes:summary', self.feed['description'])
		handler.addQuickElement(u'itunes:explicit', self.feed['iTunes_explicit'])
		handler.startElement(u"itunes:owner", {})
		handler.addQuickElement(u'itunes:name', self.feed['iTunes_name'])
		handler.addQuickElement(u'itunes:email', self.feed['iTunes_email'])
		handler.endElement(u"itunes:owner")
		handler.addQuickElement(u'itunes:image', attrs={'href': self.feed['iTunes_image_url']})
		handler.addQuickElement(u'itunes:category', attrs={'text': self.feed['iTunes_category']})

	def add_item_elements(self,  handler, item):
		super(iTunesPodcastsFeedGenerator, self).add_item_elements(handler, item)
		handler.addQuickElement(u'itunes:summary',item['summary'])
		handler.addQuickElement(u'itunes:duration',item['duration'])
		handler.addQuickElement(u'itunes:explicit',item['explicit'])


class iTunesPodcastsFeed(Feed):
	"""
	A feed of podcasts for iTunes and other compatible podcatchers.
	"""
	settings = Podcast.objects.all()[0]
	title = settings.title
	link = settings.link
	author_name = settings.author_name
	description = settings.description
	subtitle = ''
	summary = settings.summary
	iTunes_name = settings.iTunes_name
	iTunes_email = settings.iTunes_email
	iTunes_image_url = u'http://dtrhradio.com/static/dtrh/img/dtrh_logo.jpg'
	iTunes_explicit = u'no'
	feed_type = iTunesPodcastsFeedGenerator
	feed_copyright = 'Copyright %s Down the Rabbit Hole' % datetime.date.today().year

	def items(self):
		"""
		Returns a list of items to publish in this feed.
		"""
		return Episode.objects.order_by('-date_broadcast').exclude(file='')


	def feed_extra_kwargs(self, obj):
		extra = {}
		extra['iTunes_name'] = self.iTunes_name
		extra['iTunes_email'] = self.iTunes_email
		extra['iTunes_image_url'] = self.iTunes_image_url
		extra['iTunes_explicit'] = self.iTunes_explicit
		extra['iTunes_category'] = 'Arts'
		return extra

	def audio_duration(self, item):
		audio = MP3(settings.MEDIA_ROOT + '/' + str(item.file))
		m, s = divmod(audio.info.length, 60)
		h, m = divmod(m, 60)
		return '%d:%02d:%02d' % (h, m, s)

	def item_extra_kwargs(self, item):
		return {'summary': item.description, 'duration': self.audio_duration(item), 'explicit': 'no'}

	def item_pubdate(self, item):
		return item.date_broadcast

	def item_enclosure_url(self, item):
		return 'http://dtrhradio.com/media/' + str(item.file)

	def item_enclosure_length(self, item):
		length = os.path.getsize(settings.MEDIA_ROOT + '/' + str(item.file))
		return length

	def item_enclosure_mime_type(self, item):
		return 'audio/mp3'

	def item_description(self, item):
		return item.description