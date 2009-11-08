from django.conf.urls.defaults import *

urlpatterns = patterns('djortunes.fortunes.views',
    url(r'^(?P<ftype>(top|worst)?)$', 'index', name = "fortunes-index"),
    url(r'^new$', 'new', name = "fortune-new"),
    url(r'^show/(?P<fortune_id>\d+)$', 'detail', name = "fortune-detail"),
    url(r'^vote/(?P<fortune_id>\d+)/(?P<direction>(up|down))$', 'vote', name = "fortune-vote"),
)