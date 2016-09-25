"""dtrh URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from filebrowser.sites import site
from podcast import views

urlpatterns = [
    url(r'^admin/filebrowser/', include(site.urls)),
	url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^episodes/', include('podcast.urls')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'', include('pages.urls')),
    url(r'^blog/$', views.post_list, name='post_list'),
    url(r'^blog/(?P<year>\d+)/(?P<month>\d+)/(?P<slug>[-\w]+)/$', views.post, name='post'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)