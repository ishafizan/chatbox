# -*- coding: utf-8 -*-
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import sys
from json import dumps, loads
from django.core.serializers.json import DjangoJSONEncoder

try:
    sys.path.append(settings.BASE_DIR)
    from utils import util_log
    # instantiate logger
    log = util_log.logger()
except ImportError:
    raise Exception("import util files failed")


# ----------------------------------
# Create chat
# ----------------------------------
@csrf_exempt
def create_chat(request):
    body_unicode = loads(request.body.decode('utf-8'))
    log.info(dumps(body_unicode))
    mymessage = body_unicode["mymessage"]
    userid = body_unicode["userid"]

    outdata = {"status_code": 200}

    # insert into database

    response = get_response(request, outdata)
    return response


# ---------------------------------------------
# contruct json response
# ---------------------------------------------
def get_response(request, outdata):
    if request.method == 'POST':
        callback = request.GET.get('callback')
    else:
        callback = ""

    if callback != "" and callback:
        data = '%s(%s);' % (callback, dumps(outdata, indent=4))
        response = HttpResponse(data, content_type="application/json")
    else:
        response = HttpResponse(
            content=dumps(outdata, cls=DjangoJSONEncoder, indent=4), content_type="application/json"
        )
    return response
