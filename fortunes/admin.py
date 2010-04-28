from fortunes.models import Fortune
from django.contrib import admin

class FortuneAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'content', 'votes')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('pub_date',)
        }),
    )
    list_display = ('title', 'slug', 'author', 'votes')
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Fortune, FortuneAdmin)