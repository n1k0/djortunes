from djortunes.fortunes.models import Fortune, Comment
from django.contrib import admin

#class FortuneAdmin(admin.ModelAdmin):
#    fields = ['title', 'content', 'author', 'pub_date']

admin.site.register(Fortune)
admin.site.register(Comment)