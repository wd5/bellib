# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *

urlpatterns = patterns('profiles.views',
    url(r'facebook/new-user/$', 'facebook_new_user', name='facebook_new_user'),
    url(r'facebook/complite/$', 'facebook_complite', name='facebook_complite'),
#    url(r'^create/$', 'profile_create', name='profile_create'),
#    url(r'^delete/$', 'profile_delete', name='profile_delete'),
#    url(r'^edit/$', 'profile_edit', name='profile_edit'),
)