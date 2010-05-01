from django.contrib.syndication.views import Feed
from django.shortcuts import get_object_or_404
from django.conf import settings
from django_fortunes.models import Fortune
from django_fortunes.templatetags.fortune_extras import fortunize

class FortuneFeed(Feed):
    author_name = 'The django_fortunes application'
    link = 'http://github.com/n1k0/djortunes'
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
    link = "/fortunes/"
    description = "Latest fortunes added."

    def items(self):
        return self.manager.latest(getattr(settings, 'FORTUNES_MAX_PER_PAGE', 5))

class LatestFortunesByAuthor(FortuneFeed):
    title = "Latest fortunes by XXX"
    link = "/fortunes/"
    description = "Latest fortunes added by XXX."

    def items(self):
        return self.manager.latest_by_author('XXX', getattr(settings, 'FORTUNES_MAX_PER_PAGE', 5))