# -*- coding: utf-8 -*-
import logging
import os.path
import sys
from json import dumps, loads
from time import time
import requests
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

try:
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.append(BASE_DIR)
    from workers import settings
    from workers import util_es
except ImportError as err:
    logger.error(err)
    raise Exception("import util files failed")


# ----------------------------------------------
# generic command to elasticsearch
# ----------------------------------------------
@settings.app.task(name="es_insert_generic", default_retry_delay=60, max_retries=3, acks_late=True, serializer='json')
def es_insert_generic(data_out, es_target):
    try:
        # initialise elasticsearch client
        es_client = util_es.init_es(logger, es_target["es_target"], es_target["es_target"],
                                    es_target["my_index"],
                                    es_target["my_index"])

        util_es.insert_es_generic(logger, data_out, es_client["es_target_client"],
                                  es_target["my_index"])

    except Exception as error:
        logger.error(error)
        raise ValueError("es_insert_generic failed")
