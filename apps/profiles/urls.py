# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns('apps.profiles.views',
    url(r'facebook/new-user/$', 'facebook_new_user', name='facebook_new_user'),
    url(r'facebook/complite/$', 'facebook_complite', name='facebook_complite'),
)