# -*- coding: utf-8 -*-

import sys
import os.path
from os import path

try:
    from local_settings import *
except :
    raise 'local_settings.py doesn\'t exists in project root.'

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
#    ('Kuzmin Alexei', 'DrMartiner@GMail.Com'),
)
MANAGERS = ADMINS



TIME_ZONE = 'America/Chicago'
LANGUAGE_CODE = 'ru-RU'

SITE_ID = 1
USE_I18N = True
USE_L10N = True

PROJECT_ROOT = os.path.normpath(os.path.dirname(__file__)) # Глобальный путь до проекта.
sys.path.insert(0, os.path.join(PROJECT_ROOT, 'libs')) # Путь до библиотек.
sys.path.insert(0, os.path.join(PROJECT_ROOT, 'apps')) # Путь до приложений проекта.

SITE_NAME = path.basename(path.realpath(path.curdir))
SITE_ROOT = os.path.join(path.realpath(path.pardir), SITE_NAME)

MEDIA_ROOT = os.path.normpath(os.path.join(SITE_ROOT, 'media'))
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.normpath(os.path.join(SITE_ROOT, 'static'))
STATIC_URL = '/static/'

ADMIN_MEDIA_PREFIX = '/static/admin/'

STATICFILES_DIRS = (

)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)

if not DEBUG:
    TEMPLATE_LOADERS += ('django.template.loaders.eggs.Loader', )

MIDDLEWARE_CLASSES = (
    'annoying.middlewares.RedirectMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'pagination.middleware.PaginationMiddleware', # Пагинатор
    'flatpages.middleware.FlatpageFallbackMiddleware',
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

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates'),
)

INSTALLED_APPS = (
    'grappelli.dashboard',
    'grappelli',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',

    'filebrowser',
    'captcha',
    'pagination',
    'registration',
    'pytils',
    'sorl.thumbnail',
#    'south',
    'treemenus',
    'profiles',
    'social_auth',

    'flatpages',
    'simple_pages',
    'works',
    'guide',
)

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
    'profiles.backends.EmailBackend',
)

ACCOUNT_ACTIVATION_DAYS = 3

VOTE_IP_LIMITED = 5

try:
    from local_settings import *
except :
    raise 'local_settings.py doesn\'t exists in project root.'

