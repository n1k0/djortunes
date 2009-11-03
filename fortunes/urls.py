from django.conf.urls.defaults import *

urlpatterns = patterns('djortunes.fortunes.views',
    url(r'^$', 'index', name = "fortunes-index"),
    url(r'^new/$', 'new', name = "fortune-new"),
    url(r'^(?P<fortune_id>\d+)/$', 'detail', name = "fortune-detail"),
    url(r'^(?P<fortune_id>\d+)/vote/(?P<direction>(up|down))$', 'vote', name = "fortune-vote"),
)