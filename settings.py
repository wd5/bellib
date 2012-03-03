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
    # ('Your Name', 'your_email@example.com'),
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
    'django.template.loaders.eggs.Loader',
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'pagination.middleware.PaginationMiddleware', # Пагинатор
    'flatpages.middleware.FlatpageFallbackMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.request",
    "django.core.context_processors.static",
#    'social_auth.context_processors.social_auth_by_name_backends',
#    'social_auth.context_processors.social_auth_backends',
#    'social_auth.context_processors.social_auth_by_type_backends',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates')
)

INSTALLED_APPS = (
    'grappelli',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',

    'captcha',
    'pagination',
    'registration',
    'pytils',
    'sorl',
#    'south',
    'treemenus',
    'profiles',
#    'social_auth',

    'flatpages',
    'simple_pages',
    'works',
    'guide',
)

EMAIL_USE_TLS       = True
EMAIL_HOST          = 'smtp.gmail.com'
EMAIL_HOST_USER     = 'topay.po@gmail.com'
EMAIL_HOST_PASSWORD = 'good_stap'
EMAIL_PORT          = 587
EMAIL_ADDRESS_FROM  = 'topay.po@gmail.com'

GRAPPELLI_ADMIN_TITLE = 'Края лучше.NET'

AUTH_PROFILE_MODULE = 'profiles.Profile'

AUTHENTICATION_BACKENDS = (
    'profiles.backends.EmailBackend',
#    'social_auth.backends.twitter.TwitterBackend',
#    'social_auth.backends.facebook.FacebookBackend',
#    'social_auth.backends.google.GoogleOAuthBackend',
#    'social_auth.backends.google.GoogleOAuth2Backend',
#    'social_auth.backends.google.GoogleBackend',
#    'django.contrib.auth.backends.ModelBackend',
)

#SOCIAL_AUTH_ENABLED_BACKENDS = ('google', 'google-oauth', 'facebook', )
#
#TWITTER_CONSUMER_KEY         = ''
#TWITTER_CONSUMER_SECRET      = ''
#FACEBOOK_APP_ID              = ''
#FACEBOOK_API_SECRET          = ''
#GOOGLE_CONSUMER_KEY          = ''
#GOOGLE_CONSUMER_SECRET       = ''
#GOOGLE_OAUTH2_CLIENT_ID      = ''
#GOOGLE_OAUTH2_CLIENT_SECRET  = ''
#
#LOGIN_URL = '/no-login/'
#LOGIN_REDIRECT_URL = '/logged-in/'
#LOGIN_ERROR_URL = '/login-error/'
#
#SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/another-login-url/'
#SOCIAL_AUTH_NEW_USER_REDIRECT_URL = '/new-users-redirect-url/'
#SOCIAL_AUTH_NEW_ASSOCIATION_REDIRECT_URL = '/new-association-redirect-url/'
#SOCIAL_AUTH_DISCONNECT_REDIRECT_URL = '/account-disconnected-redirect-url/'
#SOCIAL_AUTH_ERROR_KEY = 'social_errors'
#
#SOCIAL_AUTH_COMPLETE_URL_NAME  = 'socialauth_complete'
#SOCIAL_AUTH_ASSOCIATE_URL_NAME = 'socialauth_associate_complete'

#SOCIAL_AUTH_DEFAULT_USERNAME = 'new_social_auth_user'

ACCOUNT_ACTIVATION_DAYS = 3

VOTE_IP_LIMITED = 5

try:
    from local_settings import *
except :
    raise 'local_settings.py doesn\'t exists in project root.'