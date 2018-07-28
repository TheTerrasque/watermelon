from django.contrib import admin

# Register your models here.
from .models import Song, SongStatus
from .models import Platform

admin.site.register(Song)
admin.site.register(SongStatus)
admin.site.register(Platform)
