from pgintranet.settings import *

import os

DEBUG = True
HOME = os.path.expanduser("~")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '${djangodb:db}',
        'USER': '${djangodb:dbusr}',
        'PASSWORD': '${djangodb:dbpwd}',
        'HOST': '',
        'PORT': '',
        }
}

AUTHENTICATION_BACKENDS = ('pgauth.remoteuserbackend.RemoteUserBackend',) + \
    AUTHENTICATION_BACKENDS

PG_CACHE_SECONDS = 300
CACHES = {
    'default': {
        'KEY_PREFIX': 'ACC_',
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:${memcached:port}',
        'OPTIONS': {
            'MAX_ENTRIES': 300000,
            'CULL_FREQUENCY': 2
        }
    }
}

MEDIA_ROOT = PROJECT_ROOT + '/var/data/media'
SERVE_MEDIA = False

HAYSTACK_CONNECTIONS['default']['URL'] = 'http://127.0.0.1:${solr:port}/solr/'
TEXT_EXTRACTION_URL = "http://127.0.0.1:${solr:port}/solr/update/extract" 
LOGGING['handlers']['default']['filename'] = "%s/var/log/djinn.log" % HOME
