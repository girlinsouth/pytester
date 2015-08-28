from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'pybug.index.index', name='index'),
    url(r'^pybug/', include('pybug.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
