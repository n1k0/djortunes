from fortunes.models import Fortune
from django.contrib import admin

class FortuneAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('title', 'content', 'votes')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('pub_date',)
        }),
    )
    list_display = ('title', 'author', 'votes')

admin.site.register(Fortune, FortuneAdmin)