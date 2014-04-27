slstore
=======

SmallsLIVE store

To install:

```
$ mkvirtualenv slstore
$ workon slstore
$ pip install -r requirements.txt
$ python manage.py syncdb
$ python manage.py migrate
$ python manage.py runserver
```