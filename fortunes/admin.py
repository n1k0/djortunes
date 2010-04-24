from fortunes.models import Fortune
from fortunes.forms import FortuneForm
from django.contrib import admin

class FortuneAdmin(admin.ModelAdmin):
    form = FortuneForm
    prepopulated_fields = {"slug": ("title",)}
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