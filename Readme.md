# Bitpin Home Task

This project written in Python 3.11 and use Django 4.2 with sqlite database and implement required endpoints.

## run project

It is nice to create virtualenv and then run following commands:

For activate venv:
```commandline
source /path_to_venv/bin/activate
```

For install requirement packages:
```commandline
pip install -r requirements.txt
```
For migrate database:
```commandline
python manage.py migrate
```
For running project:
```commandline
python manage.py runserver

```

## Notes:
You should create a superuser for django admin panel for creating other users.

For have better performance, I use pre-calculation fields when creating or updating rates for
a post. It is nice to have it on cache (redis with enabled durability) but duo to time limits, I use 2 fields in user rate model.