# development setup

### Setup
---
#### <ins>software</ins>
- java 8
- python 3.6+
- supervisord
- Elasticsearch 6.4.1 (optional)
- RabbitMQ 3.6.10
- Celery 4.2.1
- virtualenv
- Django 2.1.1

---
### <ins>Useful Links</ins>
- [virtualenv](https://packaging.python.org/guides/installing-using-pip-and-virtualenv/)
    - https://packaging.python.org/guides/installing-using-pip-and-virtualenv/
- [Supervisord](http://supervisord.org/installing.html)

```
sudo add-apt-repository universe
sudo apt-get update
sudo apt-get install supervisor
service supervisor restart
/etc/supervisor
```
- Java 8
```
sudo add-apt-repository -y ppa:webupd8team/java
sudo apt-get update
sudo apt-get -y install oracle-java8-installer
```

- Elasticsearch
    - https://www.howtoforge.com/tutorial/ubuntu-elastic-stack/
    - https://jee-appy.blogspot.com/2018/02/setup-kibana-elastisearch.html
    - https://jee-appy.blogspot.com/2018/02/setup-kibana-elastisearch.html
- RabbitMQ
    - https://www.linode.com/docs/development/python/task-queue-celery-rabbitmq/
    - https://www.vultr.com/docs/how-to-install-rabbitmq-on-ubuntu-16-04-47
    - https://www.rabbitmq.com/management.html
    
    ```
    sudo systemctl start rabbitmq-server.service
    sudo rabbitmqctl status
    sudo rabbitmqctl add_user ooli ooli123$%^
    sudo rabbitmqctl set_user_tags ooli administrator
    sudo rabbitmqctl set_permissions -p / ooli ".*" ".*" ".*"

    ```
- Cerebro
    - https://statusengine.org/tutorials/Elasticsearch-Xenial-Install/
    - https://github.com/druzmieres/install-elastic/blob/master/install-cerebro.sh
- Celery
    - http://www.celeryproject.org/install/
    - http://docs.celeryproject.org/en/latest/userguide/application.html
    - https://www.linode.com/docs/development/python/task-queue-celery-rabbitmq/
    
    ```
    celery -A settings worker --loglevel=info -Q test,celery,auth
    celery flower -A settings --broker=amqp://ooli:ooli123$%^@http://128.199.163.9:15672// --port=5555
    ```
    
- Django
    - https://docs.djangoproject.com/en/2.1/topics/install/ 
    - https://www.digitalocean.com/community/tutorials/how-to-serve-django-applications-with-uwsgi-and-nginx-on-ubuntu-14-04
    - useful commands:
    
    ```
    pip install django-ipware
    pip install passlib
    pip install PyJWT
    pip install requests
    python manage.py runserver
    ```
- UWSGi
    - https://blog.codeship.com/getting-every-microsecond-out-of-uwsgi/ 

```
sudo systemctl start uwsgi
sudo systemctl stop|restart|status uwsgi
```
