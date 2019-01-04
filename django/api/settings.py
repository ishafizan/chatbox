# use your own settings
# python manage.py runserver

# additionals
import os
import sys
from configparser import RawConfigParser
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ----------------------------------------
# Sensitive settings into another location /etc/
# ----------------------------------------
config = RawConfigParser()
config.read(r'settings/mysettings.ini')
# SECURITY WARNING: keep the secret key used in production secret!

# ----------------------------------------------------------
# Elasticsearch
# ----------------------------------------------------------
ES_SOURCE = config.get('elasticsearch', 'ES_SOURCE')
ES_TARGET = config.get('elasticsearch', 'ES_TARGET')
ES_RECONNECT_CNT = float(config.get('elasticsearch', 'ES_RECONNECT_CNT'))
ES_REQUEST_TIMEOUT = float(config.get('elasticsearch', 'ES_REQUEST_TIMEOUT'))
ES_TARGET_INDEX_AUDIT = config.get('elasticsearch', 'ES_TARGET_INDEX_AUDIT')
