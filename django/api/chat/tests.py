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

# -------------------------------------------
# secure login
# -------------------------------------------
email = "get_from_me"
password = 'get_from_me#@!'


# login
def login_secure():
    base_url = "http://%s" % "get_from_me"
    endpoint = "auth/login/secure"
    final_url = "{0}/api/{1}/{2}/".format(base_url, "0.2", endpoint)
    payload = {'email': email, 'password': password}
    response = requests.post(final_url, data=payload)
    data_token = response.json()
    log.info(response.json())
    if data_token['status'] == 200:
        log.info("login success")
        mytoken = data_token['data']['token']['access']
        myuid = data_token['data']['userid']
        return mytoken, myuid


# create chat
def test_create_chat(mytoken, mymsg):
    base_url = "http://%s" % server
    endpoint = "chat/create"
    final_url = "{0}/api/{1}/{2}/".format(base_url, "0.2", endpoint)
    log.info(final_url)
    headers = {'Content-type': 'application/json', 'Authorization': 'Bearer: %s' % mytoken}
    payload = {
        'recipientId': 1234,
        'senderId': 1,
        'msgContent': msg
    }
    response = requests.post(final_url, json=payload, headers=headers)
    return response


# login to get token
log.info("Test: get token ...")
token, userid = login_secure()
log.info("token: %s" % token)
log.info("userid: %s" % userid)

# test creation of chat message
msg = 'Hello world test message'
res = test_create_chat(token, msg)
log.info(res.json())
