__author__ = 'ads'
from django.conf.urls import patterns, url
from zuke import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'about/$', views.about, name='about'),
                       url(r'toggle/$', views.toggle, name='toggle'))