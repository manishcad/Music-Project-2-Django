from django.contrib import admin
from .models import Songs, Album, Artist
# Register your models here.

admin.site.register(Album)
admin.site.register(Songs)
admin.site.register(Artist)
