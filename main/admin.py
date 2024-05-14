from django.contrib import admin
from .models import Photo
from .models import Review

admin.site.register(Photo)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['author', 'review_text']
    search_fields = ['author', 'review_text']
