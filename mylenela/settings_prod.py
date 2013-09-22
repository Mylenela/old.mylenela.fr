SECRET_KEY = "FUCKIT"
from mylenela.settings import *

ENV = "prod"
DEBUG = False

INSTALLED_APPS += ('storages',)

import dj_database_url
DATABASES = {'default': dj_database_url.parse(os.environ.get(
    'DATABASE_URL'))}

CACHES = {
    "default": {
        "BACKEND": "redis_cache.cache.RedisCache",
        "LOCATION": os.environ.get('REDISCLOUD_URL'),
        "OPTIONS": {
            "CLIENT_CLASS": "redis_cache.client.DefaultClient",
        }
    }
}

ALLOWED_HOSTS = [
    'www-mylenela-fr.herokuapp.com',
    'www.mylenela.fr',
    'mylenela.fr']

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = "mylenela"
