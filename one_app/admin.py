from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import *


class NewsAdmin(admin.ModelAdmin):
    """Админка носотей"""
    list_display = ("title", "date", "id")


class PostAdmin(SummernoteModelAdmin):
    list_display = ("title", "date", "id")
    summernote_fields = ('text',)


admin.site.register(News, PostAdmin)
admin.site.register(Comment)
admin.site.register(Category)
