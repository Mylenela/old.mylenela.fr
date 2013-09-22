from mylenela.settings import *

ENV = "prod"
DEBUG = False

import dj_database_url
DATABASES = {'default': dj_database_url.parse(os.environ.get(
    'HEROKU_POSTGRESQL_AMBER_URL ',
    'postgres://socketubs:@localhost/mylenela'))}
ALLOWED_HOSTS = ['localhost']
