from django.contrib import admin
from .models import Photo
from .models import Review

admin.site.register(Photo)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['author', 'review_text']
    search_fields = ['author', 'review_text']


from .models import Action
from .forms import ActionForm

class ActionAdmin(admin.ModelAdmin):
    form = ActionForm

admin.site.register(Action, ActionAdmin)

from django.contrib import admin
from .models import Service

admin.site.register(Service)

# admin.py
from django.contrib import admin
from .models import Application

@admin.action(description='Одобрить выбранные заявки')
def approve_applications(modeladmin, request, queryset):
    queryset.update(approved=True, rejected=False)
    for application in queryset:
        application.send_approval_email()

@admin.action(description='Отклонить выбранные заявки')
def reject_applications(modeladmin, request, queryset):
    queryset.update(rejected=True, approved=False)
    for application in queryset:
        application.send_rejection_email()

class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'service', 'appointment_date', 'appointment_time', 'approved', 'rejected')
    actions = [approve_applications, reject_applications]

admin.site.register(Application, ApplicationAdmin)
