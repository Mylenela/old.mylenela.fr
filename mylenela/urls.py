# -*- coding: utf-8 -*-
from django.contrib import admin
from django.conf import settings
from django.conf.urls import url
from django.conf.urls import include
from django.conf.urls import patterns
from django.conf.urls.static import static


admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', 'mylenela.pages.views.view_home', name='view_home'),
    url(r'^project/(?P<slug>[\w|\W]+)',
        'mylenela.projects.views.view_project',
        name='view_project'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^localeurl/', include('localeurl.urls')),
)

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)
