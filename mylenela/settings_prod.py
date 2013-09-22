from urlparse import urlparse

SECRET_KEY = "FUCKIT"
from mylenela.settings import *

ENV = "prod"
DEBUG = False

INSTALLED_APPS += (
    'storages',
    'redis_cache')

import dj_database_url
DATABASES = {'default': dj_database_url.parse(os.environ.get(
    'DATABASE_URL'))}

REDIS_URL = urlparse(os.environ.get('REDISCLOUD_URL', 'redis://localhost:6959'))
CACHES = {
    "default": {
        "BACKEND": "redis_cache.cache.RedisCache",
        "LOCATION": '%s:%s' % (REDIS_URL.hostname, REDIS_URL.port),
        "OPTIONS": {
            "DB": 0,
            'PASSWORD': REDIS_URL.password
        }
    }
}

ALLOWED_HOSTS = ['*']
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = "mylenela"
