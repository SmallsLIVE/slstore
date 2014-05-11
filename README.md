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
$ heroku config:set PAYPAL_API_PASSWORD='yourpassword'
$ heroku config:set PAYPAL_API_SIGNATURE='yourapisig'
$ heroku config:set PAYPAL_API_USERNAME='yourapiusername'
$ heroku config:set STRIPE_PUBLIC_KEY='yourkey'
$ heroku config:set STRIPE_SECRET_KEY='yourkey'
$ git push heroku master
$ heroku run python slstore/manage.py syncdb --noinput
$ heroku run python slstore/manage.py migrate
$ heroku run python slstore/manage.py loaddata slstore/slstore/fixtures/countries.json
$ heroku run python slstore/manage.py oscar_import_catalogue slstore/slstore/fixtures/complete-smallslive-catalog.csv
$ heroku run python slstore/manage.py oscar_import_catalogue_images slstore/slstore/fixtures/images
$ heroku run python slstore/manage.py update_index
$ heroku run python slstore/manage.py createsuperuser
```
