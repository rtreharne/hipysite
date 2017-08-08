from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
    url(r'modules/$', 'resources.views.modules', name='modules'),
    url(r'modules/(?P<slug>[-\w]+)/$', 'resources.views.module', name="module"),
    url(r'modules/(?P<module_slug>[-\w]+)/(?P<element_slug>[-\w]+)/$', 'resources.views.element', name="element"),
)