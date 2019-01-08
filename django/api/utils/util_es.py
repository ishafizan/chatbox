# -*- coding: utf-8 -*-
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from json import dumps
from time import sleep
from elasticsearch import Elasticsearch, exceptions as es_exceptions
from elasticsearch.exceptions import ConnectionError

__author__ = 'Ishafizan'


# ----------------------------------
# initialize elasticsearch client
# ----------------------------------
def init_es(log, es_source, es_target, es_source_index, es_target_index):
    try:
        es_dict = {}
        es_dict.update({"es_source_client": Elasticsearch(hosts=[{"host": es_source}], maxsize=25, timeout=60,
                                                          max_retries=2, retry_on_timeout=True),
                        "es_target_client": Elasticsearch(hosts=[{"host": es_target}], maxsize=25, timeout=60,
                                                          max_retries=2, retry_on_timeout=True),
                        "source_index": es_source_index,
                        "target_index": es_target_index})
        # log.info("es initialised ...")
        return es_dict
    except Exception as err:
        log.error(err)
        raise ConnectionError(err)


# ----------------------------------
# insert single record
# ----------------------------------
def insert_es_generic(log, update_data, es_target, target_index):
    try:
        # log.info("inserting record ...")
        res = es_target.index(index=target_index, doc_type='posts', body=update_data)
        # log.info(dumps(res))
    except Exception as err:
        log.error(err)
        raise ValueError(err)


