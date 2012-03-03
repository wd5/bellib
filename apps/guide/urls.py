# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *

urlpatterns = patterns('guide.views',
    url(r'^list/$', 'guide_list', name='guide_list'),
)