slstore
=======

SmallsLIVE store

To run locally:

```
$ mkvirtualenv slstore
$ workon slstore
$ pip install -r requirements.txt
$ python manage.py syncdb
$ python manage.py migrate
$ python manage.py runserver
```

To deploy to Heroku:

```
$ heroku create slstore
$ heroku addons:add heroku-postgresql
$ heroku config:set AWS_ACCESS_KEY_ID='yourkey'
$ heroku config:set AWS_SECRET_ACCESS_KEY='yourkey'
$ heroku config:set AWS_STORAGE_BUCKET_NAME='yourbucketname'
$ heroku config:set STRIPE_PUBLIC_KEY='yourkey'
$ heroku config:set STRIPE_SECRET_KEY='yourkey'
$ git push heroku master
$ heroku run python slstore/manage.py syncdb --noinput
$ heroku run python slstore/manage.py migrate
$ heroku run python slstore/manage.py loaddata countries.json
$ heroku run python slstore/manage.py oscar_import_catalogue slstore/fixtures/smallslive-catalog.csv
$ heroku run python slstore/manage.py createsuperuser
```

Then you need to specify which countries are shippable here:
