from django.conf.urls.default import *

urlpatterns = patterns('',
    (r'^(?P<url>.*)$', 'wes.views.page'),
)
