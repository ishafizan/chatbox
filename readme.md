# ooli development server setup

### Setup
---
#### <ins>Gitlab Administration</ins>
https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-gitlab-on-ubuntu-16-04

#### <ins>GitLab and SSH keys</ins>
To manage your GitLab projects and repositories from your local machine
https://docs.gitlab.com/ee/gitlab-basics/create-your-ssh-keys.html

#### <ins>software</ins>
- java 8
- python 3.6+
- supervisord
- Orientdb v.3.0.7
- MySql  Ver 14.14 Distrib 5.7.23
- Elasticsearch 6.4.1 (optional)
- RabbitMQ 3.6.10
- Celery 4.2.1
- virtualenv
- Django 2.1.1
- uWSGI 2.0.17.1

#### <ins>pip install</ins>
```
celery==4.2.1
Django==2.1.1
django-ipware==2.1.0
flower==0.9.2 (optional)
MySQL-python==1.2.5
passlib==1.7.1
PyJWT==1.6.4
requests==2.19.1
supervisor==3.3.1
urllib3==1.23
```



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

- [Orientdb](https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-orientdb-on-ubuntu-16-04)
    - https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-orientdb-on-ubuntu-16-04
    - https://orientdb.com/nosql/pattern-matching-with-orientdb/
    - https://www.udemy.com/orientdb-getting-started/
    
    ```
    sudo bin/server.sh
    sudo systemctl start orientdb
    sudo systemctl enable orientdb

    ```

- MySql
    - https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-18-04
    - https://www.digitalocean.com/community/tutorials/how-to-set-up-a-remote-database-to-optimize-site-performance-with-mysql-on-ubuntu-16-04
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
