from .settings import *

import dj_database_url
import mongoengine
DATABASES['default'] = "dj_database_url.config(conn_max_age=600, ssl_require=True)"
DATABASES['default']['ENGINE']=mongoengine
