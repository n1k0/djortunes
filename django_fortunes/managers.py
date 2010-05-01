import datetime

from django.db import models

class FortuneManager(models.Manager):
    def published(self):
        return self.get_query_set().filter(pub_date__lte=datetime.datetime.now())
    
    def top_authors(self, max):
        return self.get_query_set().values('author')\
                                   .annotate(nb=models.Count('id'))\
                                   .order_by('-nb')[:max]