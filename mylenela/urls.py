from django.contrib import admin
from django.conf.urls import url
from django.conf.urls import include
from django.conf.urls import patterns

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
