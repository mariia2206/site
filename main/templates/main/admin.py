from django.contrib import admin
from .models import Photo


class PhotoAdmin(admin.ModelAdmin): # Для галереи фотографий
    list_display = ['description', 'image']

admin.site.register(Photo, PhotoAdmin)

