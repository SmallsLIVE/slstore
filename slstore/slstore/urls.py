from django.conf.urls import patterns, include, url
from django.conf.urls.i18n import i18n_patterns

from django.contrib import admin
from oscar.app import application
from apps.app import shop

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'slstore.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'', include(application.urls))
)

# Prefix Oscar URLs with language codes
urlpatterns += i18n_patterns('',
    url(r'', include(shop.urls)),
)