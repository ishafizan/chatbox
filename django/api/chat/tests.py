# -*- coding: utf-8 -*-
import os
import sys
import requests
from json import dumps

try:
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # print(BASE_DIR)
    sys.path.append(BASE_DIR)
    from utils import util_log

    # instantiate logger
    log = util_log.logger()
except Exception as err:
    print(err)
except ImportError:
    raise Exception("import util files failed")

server = "localhost:8000"


# Create your tests here.

# imagine from react
# python tests.py
def test_body_json(mytoken):
    base_url = "http://%s" % server
    endpoint = "chat/create"
    final_url = "{0}/api/{1}/{2}/".format(base_url, "0.2", endpoint)
    log.info(final_url)
    headers = {'Content-type': 'application/json'}
    headers = {'Authorization': 'Bearer: %s' % mytoken}
    payload = {"mymessage": "text in chat", "userid": 1234}
    response = requests.post(final_url, json=payload, headers=headers)
    return response

mytoken = "123456789"
res = test_body_json(mytoken)
log.info(res.json())
