from django.contrib import admin
from .models import Keyword, ContentItem, Flag


@admin.register(ContentItem)
class ContentItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'source', 'last_updated']
    search_fields = ['title']          
    list_filter = ['source']


@admin.register(Flag)
class FlagAdmin(admin.ModelAdmin):
    list_display = ['id', 'keyword', 'content_item', 'score', 'status']


@admin.register(Keyword)
class KeywordAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
