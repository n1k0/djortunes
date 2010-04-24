from django.db import models
from django.utils.translation import ugettext_lazy as _

from fortunes.managers import FortuneManager

class Fortune(models.Model):
    author = models.CharField(max_length=45, blank=False)
    title = models.CharField(max_length=200, blank=False)
    slug = models.SlugField(max_length=50)
    content = models.TextField(blank=False)
    pub_date = models.DateTimeField(_('published date'))
    votes = models.IntegerField(default=0)
    
    objects = FortuneManager()
    
    def __unicode__(self):
        return _("%s, from %s") % (self.title, self.author)
    
    @models.permalink
    def get_absolute_url(self):
        return ('fortune_detail', (), {
            'slug': self.slug,
            'year': self.pub_date.year,
            'month': self.pub_date.month,
            'day': self.pub_date.day
        })
