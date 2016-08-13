from django.shortcuts import render, get_object_or_404
from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Rss201rev2Feed
from models import Episode
import datetime

def episode(request, year, month, slug):
	episode = get_object_or_404(Episode, slug=slug, date_broadcast__year=year, date_broadcast__month=month)

	return render(request, 'podcast/episode.html', {'episode': episode})


# Feed

class LatestEpisodesFeed(Feed):
	title = 'Down the Rabbit Hole Radio'
	link = '/feed/'
	description = 'Down the Rabbit Hole Radio is reet good'

	def items(self):
		return Episode.objects.order_by('-date_broadcast')[:5]

	def item_title(self, item):
		return item.title

	def item_description(self, item):
		return item.description

	#def item_enclosures(self, item):
	#	item.url = '/static/' + str(item.file)
	#	item.length = 32000
	#	item.mime_type = 'audio/mpeg'
		# copyright = '&copy; Down the Rabit Hole Radio 2016'
	#	return [item]

	def item_enclosure_url(self, item):
		url = '/static/' + str(item.file)

	def item_enclosure_length(self, item):
		return 32000

	item_enclosure_mime_type = "audio/mpeg"

	feed_copyright = '&copy; Down the Rabit Hole Radio ' + str(datetime.date.today().year)

	def item_pubdate(self, item):
		return item.date_broadcast


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
		handler.addQuickElement(u'itunes:image', self.feed['iTunes_image_url'])

	def add_item_elements(self,  handler, item):
		super(iTunesPodcastsFeedGenerator, self).add_item_elements(handler, item)
		handler.addQuickElement(u'iTunes:summary',item['summary'])
		handler.addQuickElement(u'iTunes:duration',item['duration'])
		handler.addQuickElement(u'iTunes:explicit',item['explicit'])


#class iTunesPodcastPost(request, id):
#	podcast = get_object_or_404(Episode, id=id)
#
#	def __init__(self, podcast):
#		self.id = podcast.id
#		self.date_broadcast = podcast.date_broadcast
#		self.title = podcast.title
#		self.summary = podcast.description
#		self.enclosure_url = podcast.file.url
#		self.enclosure_length = podcast.file.size
#		self.enclosure_mime_type = u'audio/mpeg'
#		self.duration = '10'
#		self.explicit = u'no'
#
#	def __unicode__(self):
#		return "Podcast: %s" % self.title
#
#	def get_absolute_url(self):
#		return ('itunes_episode', [str(self.id)])


class iTunesPodcastsFeed(Feed):
	"""
	A feed of podcasts for iTunes and other compatible podcatchers.
	"""
	title = "iTunes Podcast"
	link = "/podcasts/iTunes/"
	author_name = 'The Great Author'
	description = "A Podcast of great things."
	subtitle = "From now until forever"
	summary = "People get around and chat about stuff.  You listen."
	iTunes_name = u'author Name'
	iTunes_email = u'[email protected]'
	iTunes_image_url = u'http://example.com/url/of/image'
	iTunes_explicit = u'no'
	feed_type = iTunesPodcastsFeedGenerator
	feed_copyright = "Copyright %s by the The Author." % datetime.date.today().year

	def items(self):
		"""
		Returns a list of items to publish in this feed.
		"""
		return Episode.objects.order_by('-date_broadcast')[:5]


	def feed_extra_kwargs(self, obj):
		extra = {}
		extra['iTunes_name'] = self.iTunes_name
		extra['iTunes_email'] = self.iTunes_email
		extra['iTunes_image_url'] = self.iTunes_image_url
		extra['iTunes_explicit'] = self.iTunes_explicit
		return extra

	def item_extra_kwargs(self, item):
		return {'summary': item.description, 'duration': '1200', 'explicit': 'no'}

	def item_pubdate(self, item):
		return item.date_broadcast

	def item_enclosure_url(self, item):
		return '/static/' + str(item.file)

	def item_enclosure_length(self, item):
		return 1200

	def item_enclosure_mime_type(self, item):
		return 'audio/mp3'

	def item_description(self, item):
		return item.description