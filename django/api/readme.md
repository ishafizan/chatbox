# Tips

---
#### <ins>Django</ins>
- create project api
```
django-admin startproject api
```
- edit settings.py
- edit urls/py
- edit chat/urls.py
- create additional folders, add additional files

- python manage.py runserver
- http://localhost:8000/api/0.2/chat/create/
- payload example (from RN)
```
{"mymessage": "text in chat", "userid": 1234}
```

once ok, can consider elasticsearch inserts via rabbitmq, celery
