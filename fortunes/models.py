from django.db import models

class Fortune(models.Model):
    author = models.CharField(max_length=45, blank=False)
    title = models.CharField(max_length=200, blank=False)
    content = models.TextField(blank=False)
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    votes = models.IntegerField(default=0)
    
    def __unicode__(self):
        return "%s, from %s" % (self.title, self.author)

class Comment(models.Model):
    fortune = models.ForeignKey(Fortune, blank=False)
    author = models.CharField(max_length=45, blank=False)
    content = models.CharField(max_length=500, blank=False)
    pub_date = models.DateTimeField('date published', auto_now_add=True)

    def __unicode__(self):
        return "comment from %s on %s" % (self.author, self.fortune.title)
