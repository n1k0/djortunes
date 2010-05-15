import datetime

from django.db import models
from django.contrib.contenttypes.models import ContentType

class FortuneManager(models.Manager):
    def latest(self):
        "Generates a query to retrieve latest fortunes"
        return self.published().order_by('-pub_date')

    def latest_by_author(self, author):
        "Generates a query to retrieve latest fortunes by a given author"
        return self.published().filter(author__username=author).order_by('-pub_date')

    def published(self):
        "Generates a query to retrieve published fortunes"
        return self.get_query_set().filter(pub_date__lte=datetime.datetime.now())
    
    def top_authors(self):
        "Generates a query to retrieve top fortune authors"
        return self.published().values('author__username')\
                               .annotate(nb=models.Count('id'))\
                               .order_by('-nb')
