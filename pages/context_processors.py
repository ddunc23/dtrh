from pages.models import Page

def menu_links(request):
	menu_links = Page.objects.all().order_by('title')
	return {'menu_links': menu_links}