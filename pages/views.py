from django.shortcuts import render
from models import Page

def site_home(request):
	return render(request, 'pages/index.html')

def page(request, slug):
	page = Page.objects.get(slug=slug)
	return render(request, 'pages/page.html', {'page': page})
