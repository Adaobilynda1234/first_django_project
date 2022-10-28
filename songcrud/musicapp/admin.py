from django.contrib import admin
from .models import song, Artiste, Lyric

# Register your models here.
admin.site.register(song)
admin.site.register(Artiste)
admin.site.register(Lyric)
