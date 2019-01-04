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
- payload example (from RN)
```
- http://localhost:8000/api/0.2/chat/create/
{"mymessage": "text in chat", "userid": 1234}
```

once ok, can consider elasticsearch inserts via rabbitmq, celery
