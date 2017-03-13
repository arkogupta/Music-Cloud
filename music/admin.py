from django.contrib import admin
from .models import Album,Song




# Register your models here.

admin.site.register(Album) #register the album class on the admin page
admin.site.register(Song)

