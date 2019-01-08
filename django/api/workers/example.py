# -*- coding: utf-8 -*-
from workers import tasks

# run this
# celery -A settings worker --loglevel=info -Q test,celery,chat

# specify Q of which workers to greedily look at
queue_name = "chat"

# specify server & index_name
es_target = {"es_target": "localhost", "index": "my_index"}

try:
    # set you data structures to be inserted
    data_out = {"id" : "your_data_dicts"}
    print("Sending task to queue_name: %s " % queue_name)
    
    tasks.es_insert_generic.apply_async(args=[data_out, es_target],
                                        expires=1 * 60,
                                        queue=queue_name)
except Exception as err:
    print(err)

