SECRET_KEY = "FUCKIT"
from mylenela.settings import *

ENV = "dev"
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME':  os.path.join(SITE_ROOT, 'mylenela.db'),
    }
}

INSTALLED_APPS += ('debug_toolbar',)

MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

DEBUG_TOOLBAR_PANELS = (
    'debug_toolbar.panels.version.VersionDebugPanel',
    'debug_toolbar.panels.timer.TimerDebugPanel',
    'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
    'debug_toolbar.panels.headers.HeaderDebugPanel',
    #'debug_toolbar.panels.profiling.ProfilingDebugPanel',
    'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
    'debug_toolbar.panels.sql.SQLDebugPanel',
    'debug_toolbar.panels.template.TemplateDebugPanel',
    'debug_toolbar.panels.cache.CacheDebugPanel',
    'debug_toolbar.panels.signals.SignalDebugPanel',
    'debug_toolbar.panels.logger.LoggingPanel',
)
DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}
INTERNAL_IPS = ('127.0.0.1', '203.35.33.226')
TAG = 'body'

STATIC_ROOT = os.path.join(SITE_ROOT, "static")
STATICFILES_DIRS = (
    os.path.join(SITE_ROOT, "mylenela", "assets"),
)

LOCALE_INDEPENDENT_PATHS = (
    r'^/static',
    r'^/media',
)

ALLOWED_HOSTS = ['localhost']
