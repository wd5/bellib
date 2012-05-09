# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from registration.forms import RegistrationFormUniqueEmail
from filebrowser.sites import site
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'apps.simple_pages.views.main_page', name='main_page'),
    url(r'^login/$', 'apps.simple_pages.views.login_page', name='login_page'),

    (r'^works/', include('apps.works.urls')),
    (r'^guide/', include('apps.guide.urls')),
    (r'^profile/', include('apps.profiles.urls')),

    url(r'^accounts/register/$', 'registration.views.register',
            {'form_class': RegistrationFormUniqueEmail, 'backend': 'registration.backends.default.DefaultBackend', },
        name='registration_register'
    ),
    url(r'^accounts/login/$', 'apps.profiles.views.login_by_email', name='auth_login'),
    (r'^accounts/', include('registration.backends.default.urls')),

    (r'^admin/', include(admin.site.urls)),
    (r'^grappelli/?', include('grappelli.urls')),
    url(r'^admin/filebrowser/', include(site.urls)),

    url(r'', include('social_auth.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True, }),
        (r'^static/(.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT, 'show_indexes': True, }),
    )