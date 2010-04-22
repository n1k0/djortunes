from django.db import models
from django.db.models import Avg, Max, Min, Count

class Fortune(models.Model):
    author = models.CharField(max_length=45, blank=False)
    title = models.CharField(max_length=200, blank=False)
    content = models.TextField(blank=False)
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    votes = models.IntegerField(default=0)
    
    def __unicode__(self):
        return "%s, from %s" % (self.title, self.author)

    @staticmethod
    def top_authors(max):
        return Fortune.objects.values('author').annotate(nb=Count('id')).order_by('-nb')[:max]

class Comment(models.Model):
    fortune = models.ForeignKey(Fortune, blank=False)
    author = models.CharField(max_length=45, blank=False)
    content = models.TextField(blank=False)
    pub_date = models.DateTimeField('date published', auto_now_add=True)

    def __unicode__(self):
        return "comment from %s on %s" % (self.author, self.fortune.title)
