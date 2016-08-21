from django.conf.urls import include, url
import views

urlpatterns = [
	url(r'(?P<year>\d+)/(?P<month>\d+)/(?P<slug>[-\w]+)/$', views.episode, name='podcast-episode'),
	# Feed
	url(r'latest/feed/itunes/$', views.iTunesPodcastsFeed(), name='itunes_feed'),
]