from podcast.models import Episode
import datetime

def blog_post_list(request):
	blog_post_list = episodes = Episode.objects.filter(file='', date_broadcast__lte=datetime.date.today()).order_by('-date_broadcast')
	return {'blog_post_list': blog_post_list}