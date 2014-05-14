slstore
=======

SmallsLIVE store

To run locally
--------------

These instructions are assuming that you've installed virtualenv and virtualenvwrapper.

```
$ mkvirtualenv slstore
$ workon slstore
$ pip install -r requirements.txt
$ python manage.py syncdb
$ python manage.py migrate
$ python manage.py loaddata slstore/fixtures/countries.json
$ python manage.py oscar_import_catalogue slstore/fixtures/complete-smallslive-catalog.csv
$ python manage.py oscar_import_catalogue_images slstore/fixtures/images
$ python manage.py update_index
$ python manage.py runserver
```

You'll also need to set some environment variables. The easiest way to do this is to add these lines to the file `~/.virtualenvs/slstore/bin/postactivate`:

```
export AWS_ACCESS_KEY_ID='yourkey'
export AWS_SECRET_ACCESS_KEY='yourkey'
export AWS_STORAGE_BUCKET_NAME='yourbucketname'
export PAYPAL_API_PASSWORD='yourpassword'
export PAYPAL_API_SIGNATURE='yourapisig'
export PAYPAL_API_USERNAME='yourapiusername'
export STRIPE_PUBLIC_KEY='yourkey'
export STRIPE_SECRET_KEY='yourkey'
```

And then re-run `workon slstore` to run the postactivate script.

To deploy to Heroku
-------------------

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

You only need to run the `config:set` commands once, the first time you deploy. These values will persist for subsequent deploys.
