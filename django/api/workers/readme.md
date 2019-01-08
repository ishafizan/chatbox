# ----------------------------------------#
# Celery
# this folder can be deployed on other worker servers
# start and controllable via supervisor
# note: each Q can have their own workers
# ----------------------------------------#

```
celery -A settings worker --loglevel=info -Q test,celery,chat
```
