from django.contrib.syndication.feeds import Feed, FeedDoesNotExist
from django.contrib.sites.models import Site
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.core.urlresolvers import reverse

from django_fortunes.models import Fortune
from django_fortunes.templatetags.fortune_extras import fortunize

class FortuneFeed(Feed):
    author_name = 'The django_fortunes application'
    _site = Site.objects.get_current()
    manager = Fortune.objects

    def item_author_name(self, item):
        return item.author

    def item_description(self, item):
        return fortunize(item.content)

    def item_link(self, item):
        return item.get_absolute_url()

    def item_pubdate(self, item):
        return item.pub_date

    def item_title(self, item):
        return item.title

class LatestFortunes(FortuneFeed):
    title = "Latest fortunes"
    description = "Latest fortunes added."

    def items(self):
        return self.manager.latest()

    def link(self, obj):
        return reverse('fortune_index_type', kwargs={'order_type': 'latest'})

class LatestFortunesByAuthor(FortuneFeed):
    def get_object(self, bits):
        ''' Retrieve simple param in url, waiting for authenticated user '''
        if len(bits) != 1:
            raise ObjectDoesNotExist
        return bits[0]

    def title(self, obj):
        return "Latest fortunes by %s" % obj

    def link(self, obj):
        if not obj:
            raise FeedDoesNotExist
        return reverse('fortune_index_author', kwargs={'author': obj})

    def description(self, obj):
        return "Latest fortunes added by %s." % obj

    def items(self, obj):
        return self.manager.latest_by_author(obj)[:getattr(settings, 'FORTUNES_MAX_PER_PAGE', 5)]