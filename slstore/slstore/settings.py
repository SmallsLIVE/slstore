import os
import dj_database_url

# Django settings for oscar project.
PROJECT_DIR = os.path.dirname(__file__)
location = lambda x: os.path.join(os.path.dirname(os.path.realpath(__file__)), x)

DEBUG = True
TEMPLATE_DEBUG = True
SQL_DEBUG = True

ADMINS = (
    ('Nate Aune', 'smallslive@appsembler.com'),
)

MANAGERS = ADMINS

EMAIL_SUBJECT_PREFIX = '[SmallsLIVE] '

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

if os.environ.get('DATABASE_URL'):
    DATABASES = {'default': dj_database_url.config(default='postgres://nateaune@localhost:5432/smallslivestore')}
else:
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': location("db.sqlite"),
        'ATOMIC_REQUESTS': True,  # Django 1.6+
        'TIMEOUT': 20,
    }
}
ATOMIC_REQUESTS = True

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/New_York'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

USE_TZ = True

gettext_noop = lambda s: s
LANGUAGES = (
    ('en-us', gettext_noop('American English')),
    ('en-gb', gettext_noop('British English')),
    ('zh-cn', gettext_noop('Simplified Chinese')),
    ('nl', gettext_noop('Dutch')),
    ('it', gettext_noop('Italian')),
    ('pl', gettext_noop('Polish')),
    ('ru', gettext_noop('Russian')),
    ('sk', gettext_noop('Slovak')),
    ('pt-br', gettext_noop('Brazilian Portuguese')),
    ('fr', gettext_noop('French')),
    ('de', gettext_noop('German')),
    ('ko', gettext_noop('Korean')),
    ('uk', gettext_noop('Ukrainian')),
    ('es', gettext_noop('Spanish')),
    ('da', gettext_noop('Danish')),
    ('ar', gettext_noop('Arabic')),
    ('ca', gettext_noop('Catalan')),
    ('cs', gettext_noop('Czech')),
    ('el', gettext_noop('Greek')),
)

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = location("public/media")

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
#ADMIN_MEDIA_PREFIX = '/media/admin/'

STATIC_URL = '/static/'
STATIC_ROOT = location('public')


STATICFILES_DIRS = (
    location('static/'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = os.environ.get("SECRET_KEY", "herokudefault")

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.request",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    # Oscar specific
    'oscar.apps.search.context_processors.search_form',
    'oscar.apps.promotions.context_processors.promotions',
    'oscar.apps.checkout.context_processors.checkout',
    'oscar.apps.customer.notifications.context_processors.notifications',
    'oscar.core.context_processors.metadata',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
#    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'oscar.apps.basket.middleware.BasketMiddleware',
)

INTERNAL_IPS = ('127.0.0.1',)

ROOT_URLCONF = 'slstore.urls'

from oscar import OSCAR_MAIN_TEMPLATE_DIR
TEMPLATE_DIRS = (
    location('templates'),
    os.path.join(OSCAR_MAIN_TEMPLATE_DIR, 'templates'),
    OSCAR_MAIN_TEMPLATE_DIR,
)


INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.flatpages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    # External apps
    'django_extensions',
#    'debug_toolbar',
    # Apps from oscar
    'paypal',
    'south',
    'compressor'
]

from oscar import get_core_apps
INSTALLED_APPS = INSTALLED_APPS + get_core_apps([
    'slstore.apps.shipping',
    'slstore.apps.checkout'])

AUTHENTICATION_BACKENDS = (
    'oscar.apps.customer.auth_backends.Emailbackend',
    'django.contrib.auth.backends.ModelBackend',
)

LOGIN_REDIRECT_URL = '/accounts/'
APPEND_SLASH = True

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False
}

# Oscar settings
from oscar.defaults import *

OSCAR_SHOP_TAGLINE = 'SmallsLIVE'
OSCAR_RECENTLY_VIEWED_PRODUCTS = 20
OSCAR_ALLOW_ANON_CHECKOUT = True
OSCAR_DEFAULT_CURRENCY = "USD"
OSCAR_FROM_EMAIL = "smallslive@appsembler.com"

# Order processing
# ================

# Some sample order/line status settings
OSCAR_INITIAL_ORDER_STATUS = 'Pending'
OSCAR_INITIAL_LINE_STATUS = 'Pending'
OSCAR_ORDER_STATUS_PIPELINE = {
    'Pending': ('Being processed', 'Cancelled',),
    'Being processed': ('Processed', 'Cancelled',),
    'Cancelled': (),
    'Processed': (),
}

# Taken from PayPal's documentation - these should always work in the sandbox
PAYPAL_SANDBOX_MODE = True
PAYPAL_CALLBACK_HTTPS = False
PAYPAL_API_VERSION = '88.0'

# These are the standard PayPal sandbox details from the docs - but I don't
# think you can get access to the merchant dashboard.
PAYPAL_API_USERNAME = os.environ.get("PAYPAL_API_USERNAME", "")
PAYPAL_API_PASSWORD = os.environ.get("PAYPAL_API_PASSWORD", "")
PAYPAL_API_SIGNATURE = os.environ.get("PAYPAL_API_SIGNATURE", "")


# Standard currency is GBP
PAYPAL_CURRENCY = PAYPAL_PAYFLOW_CURRENCY = 'USD'

PAYPAL_PAYFLOW_DASHBOARD_FORMS = True

# Add Payflow dashboard stuff to settings
from django.utils.translation import ugettext_lazy as _
OSCAR_DASHBOARD_NAVIGATION.append(
    {
        'label': _('PayPal'),
        'icon': 'icon-globe',
        'children': [
            {
                'label': _('PayFlow transactions'),
                'url_name': 'paypal-payflow-list',
            },
            {
                'label': _('Express transactions'),
                'url_name': 'paypal-express-list',
            },
        ]
    })


# Haystack settings
# HAYSTACK_CONNECTIONS = {
#     'default': {
#         'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
#     },
# }

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': os.path.join(os.path.dirname(__file__), 'whoosh_index'),
    },
}


ALLOWED_HOSTS = ['*']

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Django storages / S3
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
AWS_S3_SECURE_URLS = False
AWS_QUERYSTRING_AUTH = False

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'django.utils.log.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['null'],
            'propagate': True,
            'level': 'INFO',
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
        'oscar.checkout': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'INFO',
        },
        'django.db.backends': {
            'handlers': ['null'],
            'propagate': False,
            'level': 'DEBUG',
        },
        'paypal.express': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'DEBUG',
        },
        'paypal.payflow': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'DEBUG',
        },
    }
}

# Put your own sandbox settings into an integration.py modulde (that is ignored
# by git).
try:
    from integration import *
except ImportError:
    pass

