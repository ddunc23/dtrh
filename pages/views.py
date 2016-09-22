from django.shortcuts import render
from models import Page
from podcast.models import Episode

def site_home(request):
	latest = Episode.objects.exclude(file='').order_by('-date_broadcast').first()
	return render(request, 'pages/index.html', {'latest': latest})

def page(request, slug):
	page = Page.objects.get(slug=slug)
	return render(request, 'pages/page.html', {'page': page})
