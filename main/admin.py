from django.contrib import admin
from .models import Song
from .forms import DownloadForm
# Register your models here.

class SongAdmin(admin.ModelAdmin):
    list_display = ("link", 'created_at')
    readonly_fields = ("link", 'created_at')
    # fields = ['link', 'created_at',]


admin.site.register(Song, SongAdmin)