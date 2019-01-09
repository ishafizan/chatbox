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
    from workers import tasks

    # instantiate logger
    log = util_log.logger()
except ImportError:
    raise Exception("import util files failed")


# ----------------------------------
# Create chat
# ----------------------------------
@csrf_exempt
def create_chat(request):
    status_code = 400
    body_unicode = loads(request.body.decode('utf-8'))
    # log.info(dumps(body_unicode))
    recipient_id = body_unicode["recipientId"]
    sender_id = body_unicode["senderId"]
    msg = body_unicode["msgContent"]

    log.info("recipientId: %s" % recipient_id)
    log.info("senderId: %s" % sender_id)
    log.info("msgContent: %s" % msg)

    # prepare data for insertion into es
    data_out = {"recipient_id": recipient_id, "ip": sender_id,
                "msg": msg}

    try:
        """
        queue_name = "chat"
        # specify server & index_name
        es_target = {"es_target": "localhost", "index": "my_index"}
        # set you data structures to be inserted
        log.info("Sending task to queue_name: %s " % queue_name)
        tasks.es_insert_generic.apply_async(args=[data_out, es_target],
                                            expires=1 * 60,
                                            queue=queue_name)
        """
        status_code = 200
        resp_msg = "chat inserted"
    except Exception as err:
        log.error(err)
        resp_msg = err

    resp_data = {"status_code": status_code, "msg": resp_msg}
    response = get_response(request, resp_data)
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
