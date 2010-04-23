from django.conf.urls.defaults import *
from django.conf import settings

from fortunes.views import fortune_list, fortune_detail, fortune_vote, fortune_new

urlpatterns = patterns('',
    url(r'^$', fortune_list, name='fortune_index'),
    url(r'^(?P<order_type>(top|worst)?)/(?P<page>\w)?$', fortune_list, name='fortune_index_type'),
    url(r'^new$', fortune_new, name = 'fortune_new'),
    url(r'^show/(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<object_pk>\d+)/$', fortune_detail, name='fortune_detail'),
    url(r'^vote/(?P<object_pk>\d+)/(?P<direction>(up|down))$', fortune_vote, name='fortune_vote'),
)