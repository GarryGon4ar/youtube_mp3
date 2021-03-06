from django.contrib import admin
from .models import Song


class SongAdmin(admin.ModelAdmin):
    list_display = ("link", "created_at")
    readonly_fields = ("link", "created_at")


admin.site.register(Song, SongAdmin)
