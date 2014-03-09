# -*- coding: utf-8 -*-
import os
from django.utils.crypto import get_random_string

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SITE_ROOT = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..')
DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'mylenela.db',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

TIME_ZONE = 'Europe/Paris'
LANGUAGE_CODE = 'en-us'
USE_I18N = True
USE_L10N = True
USE_TZ = True

MEDIA_ROOT = os.path.join(SITE_ROOT, 'uploads')
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(SITE_ROOT, "static")
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(SITE_ROOT, "assets"),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #'django.contrib.staticfiles.finders.DefaultStorageFinder'
)

chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
SECRET_KEY = get_random_string(50, chars)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    #'django.template.loaders.eggs.Loader',
)
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'localeurl.middleware.LocaleURLMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'mylenela.urls'

WSGI_APPLICATION = 'mylenela.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(SITE_ROOT, 'templates', 'pages'),
    os.path.join(SITE_ROOT, 'templates', 'projects'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.request",
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'south',
    'localeurl',
    'mylenela.projects',
    'mylenela.pages'
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
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

try:
    from .local_settings import *
except ImportError:
    print('!! Warning! File "mylenela/local_settings.py" file is missing')
    print('!! Copy "mylenela/local_settings_example.py" to start a new one')
    exit(1)


from django.utils.translation import gettext as _
LANGUAGES = (
    ('en', _('English')),
    ('fr', _('French')),
)
DEFAULT_LANGUAGE = 1
LOCALEURL_USE_SESSION = True
TRANSMETA_LANGUAGES = LANGUAGES
TRANSMETA_DEFAULT_LANGUAGE = 'en'

LOCALE_INDEPENDENT_PATHS = (
    r'^/static',
    r'^/media',
)

LOCALE_PATHS = (os.path.join(SITE_ROOT, 'locale'),)
