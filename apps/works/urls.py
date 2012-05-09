# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns('apps.works.views',
    url(r'^ratio/$', 'works_ratio', name='works_ratio'),
    url(r'^list/$', 'works_list', name='works_list'),
    url(r'^list/search/$', 'works_list', name='works_search'),
    url(r'^apply/$', 'work_apply', name='work_apply'),
    url(r'^list/by-user/(\d+)/$', 'works_list', name='works_by_user'),
    url(r'^list/(\d+)/$', 'work_inside', name='work_inside'),
    url(r'^list/download/(\d+)/$', 'work_download', name='work_download'),
    url(r'^list/add/$', 'work_add', name='work_add'),
    url(r'^list/edit/(\d+)/$', 'work_add', name='work_edit'),
    url(r'^training/$', 'work_training', name='work_training'),
    url(r'^evaluation/set/$', 'work_set_evaluation', name='work_set_evaluation'),
)