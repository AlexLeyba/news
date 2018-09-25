from django.contrib import admin
from one_app.models import News


class NewsAdmin(admin.ModelAdmin):
    """Админка носотей"""
    list_display = ("title", "date", "id")


admin.site.register(News, NewsAdmin)
