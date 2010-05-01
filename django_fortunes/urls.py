from django.conf.urls.defaults import *
from django.conf import settings

from django_fortunes.feeds import LatestFortunes, LatestFortunesByAuthor
from django_fortunes.views import fortune_list, fortune_detail, \
                                  fortune_vote, fortune_new

feeds = {
    'latest': LatestFortunes,
    'author': LatestFortunesByAuthor,
}

urlpatterns = patterns('',
    url(r'^$',
        fortune_list,
        name='fortune_index'),
    
    url(r'^author/(?P<author>\w+)/(?P<page>\w)?$',
        fortune_list,
        name='fortune_index_author'),

    url(r'^(?P<order_type>(top|worst)?)/(?P<page>\w)?$',
        fortune_list,
        name='fortune_index_type'),
    
    url(r'^new$',
        fortune_new,
        name='fortune_new'),
    
    url(r'^show/(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<slug>[-\w]+)/$',
        fortune_detail,
        name='fortune_detail'),
    
    url(r'^vote/(?P<object_pk>\d+)/(?P<direction>(up|down))$',
        fortune_vote,
        name='fortune_vote'),
    
    url(r'^feeds/latest/$', 
        LatestFortunes(), 
        name='fortune_feed_latest'),
    
    url(r'^feeds/author/(?P<author>\w+)/$', 
        LatestFortunesByAuthor(), 
        name='fortune_feed_author'),
)