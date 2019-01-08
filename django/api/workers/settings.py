# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from __future__ import division
from __future__ import print_function
from celery import Celery

# ----------------------------------------#
# RABBITMQ
# ----------------------------------------#
RABBITMQ_IP = "localhost"
RABBITMQ_VHOST = ""
RABBITMQ_USER = "my_user"
RABBITMQ_PWD = "my_password"

# ----------------------------------------#
# Celery
# this folder can be deployed on other worker servers
# start and controllable via supervisor
# celery -A settings worker --loglevel=info -Q test,celery,auth,post,user
# note: each Q can have their own workers
# ----------------------------------------#
# amqp://ooli:%s@%s/%s
app = Celery('workers',
             broker='amqp://%s:%s@%s/%s' % (RABBITMQ_USER, RABBITMQ_PWD, RABBITMQ_IP, RABBITMQ_VHOST),
             backend='amqp://',
             include=['tasks'])


app.conf.update(
    CELERY_TASK_SERIALIZER='json',
    CELERY_RESULT_SERIALIZER='json',
    CELERY_TASK_RESULT_EXPIRES=3600,
    CELERY_ACCEPT_CONTENT=['application/json', 'pickle'],
    BROKER_TRANSPORT_OPTIONS={'confirm_publish': True},
    # CELERY_IGNORE_RESULT=True,  # ignore results & improve performance
)


if __name__ == '__main__':
    app.start()
