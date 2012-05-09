# -*- coding: utf-8 -*-

import sys
import os.path
from os import path

try:
    from local_settings import *
except :
    print 'local_settings.py doesn\'t exists in <project_root>/bellib/.'

DEBUG = False
TEMPLATE_DEBUG = DEBUG

PROJECT_ROOT = os.path.normpath(os.path.dirname(__file__)) # Глобальный путь до проекта
sys.path.insert(0, os.path.join(PROJECT_ROOT, 'apps')) # Путь до приложений проекта

SITE_NAME = path.basename(path.realpath(path.curdir))
SITE_ROOT = os.path.join(path.realpath(path.pardir), SITE_NAME)

ADMINS = (
#    ('Kuzmin Alexei', 'DrMartiner@GMail.Com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

USE_TZ = True
TIME_ZONE = 'Europe/Moscow'

SITE_ID = 1

USE_I18N = True
USE_L10N = True

USE_TZ = True

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.normpath(os.path.join(SITE_ROOT, 'media'))

STATIC_URL = '/static/'
STATIC_ROOT = os.path.normpath(os.path.join(SITE_ROOT, 'static'))
STATICFILES_DIRS = ()

ADMIN_MEDIA_PREFIX = '/static/grappelli/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

SECRET_KEY = ''

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'annoying.middlewares.RedirectMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'pagination.middleware.PaginationMiddleware', # Пагинатор
    'apps.flatpages.middleware.FlatpageFallbackMiddleware',
    'django.middleware.locale.LocaleMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.request",
    "django.core.context_processors.static",
    'django.contrib.messages.context_processors.messages',
    'social_auth.context_processors.social_auth_by_name_backends',
    'social_auth.context_processors.social_auth_backends',
    'social_auth.context_processors.social_auth_by_type_backends',
)

ROOT_URLCONF = 'bellib.urls'

WSGI_APPLICATION = 'bellib.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(SITE_ROOT, 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'grappelli',
    'django.contrib.admin',

    'filebrowser',
    'pagination',
    'registration',
    'pytils',
    'sorl.thumbnail',
    'treemenus',
    'apps.profiles',
    'social_auth',

    'apps.flatpages',
    'apps.simple_pages',
    'apps.works',
    'apps.guide',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'social_auth': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': 'logs/social_auth.log',
            'maxBytes': 1024*1024*5,
            'backupCount': 5,
            },
        },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
            },
        'SocialAuth': {
            'handlers': ['social_auth'],
            'level': 'DEBUG',
            'propagate': True,
        },
    }
}

EMAIL_USE_TLS = False
EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_HOST_USER = 'bellib-ru'
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 25
EMAIL_ADDRESS_FROM = 'bellib-ru@yandex.ru'

GRAPPELLI_ADMIN_TITLE = 'Края лучше.NET'
GRAPPELLI_INDEX_DASHBOARD = 'bellib.dashboard.CustomIndexDashboard'

DIRECTORY = 'filebrowser'
FILEBROWSER_DIRECTORY = 'filebrowser'
URL_TINYMCE = ADMIN_MEDIA_PREFIX + "tinymce/jscripts/tiny_mce/"
PATH_TINYMCE = ADMIN_MEDIA_PREFIX + "tinymce/jscripts/tiny_mce/"
TINYMCE_JS_URL = ADMIN_MEDIA_PREFIX + "tinymce/jscripts/tiny_mce/tiny_mce.js"

AUTH_PROFILE_MODULE = 'profiles.Profile'

VK_APP_ID = ''
VK_API_SECRET = ''

FACEBOOK_APP_ID = ''
FACEBOOK_API_SECRET = ''

LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/accounts/login/'
LOGIN_ERROR_URL = '/accounts/login/'

AUTHENTICATION_BACKENDS = (
    'social_auth.backends.twitter.TwitterBackend',
    'social_auth.backends.facebook.FacebookBackend',
    'social_auth.backends.contrib.vkontakte.VkontakteBackend',
    'django.contrib.auth.backends.ModelBackend',
    'apps.profiles.backends.EmailBackend',
)

ACCOUNT_ACTIVATION_DAYS = 3

VOTE_IP_LIMITED = 5

try:
    from local_settings import *
except :
    print 'local_settings.py doesn\'t exists in <project_root>/bellib/.'