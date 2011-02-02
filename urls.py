from django.conf.urls.defaults import *

urlpatterns = patterns('',
    # a little hack for making home work (for now)
    (r'^$', 'wes.views.page', { 'url':'/home/' }),
    (r'^(?P<url>.*)$', 'wes.views.page'),
)
