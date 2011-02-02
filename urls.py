from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^(?P<url>.*)$', 'wes.views.page'),
)
