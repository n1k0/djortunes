from djortunes.fortunes.models import Fortune
from django.contrib import admin

#class FortuneAdmin(admin.ModelAdmin):
#    fields = ['title', 'content', 'author', 'pub_date']

admin.site.register(Fortune)