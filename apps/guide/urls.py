# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns('apps.guide.views',
    url(r'^list/$', 'guide_list', name='guide_list'),
)