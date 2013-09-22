SECRET_KEY = "FUCKIT"
from mylenela.settings import *

ENV = "prod"
DEBUG = False

INSTALLED_APPS += ('storages',)

import dj_database_url
DATABASES = {'default': dj_database_url.parse(os.environ.get(
    'DATABASE_URL'))}
ALLOWED_HOSTS = ['localhost']

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = "mylenela"
