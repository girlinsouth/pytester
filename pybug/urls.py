from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'pybug.index.index', name='index'),
    url(r'^index/', 'pybug.index.index', name='index'),
    url(r'^allbugs/', 'pybug.index.allBugs', name='allbugs'),
)

