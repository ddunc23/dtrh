from django.conf.urls import include, url
import views

urlpatterns = [
	url(r'^$', views.episode_list, name='episode_list'),
	url(r'(?P<year>\d+)/(?P<month>\d+)/(?P<slug>[-\w]+)/$', views.episode, name='episode'),
	# Feed
	url(r'latest/feed/itunes/$', views.iTunesPodcastsFeed(), name='itunes_feed'),
]