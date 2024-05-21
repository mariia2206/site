from django.contrib import admin
from .models import Photo, Review, Action, Service, Application
from .forms import ActionForm

admin.site.register(Photo)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['author', 'review_text']
    search_fields = ['author', 'review_text']

class ActionAdmin(admin.ModelAdmin):
    form = ActionForm

admin.site.register(Action, ActionAdmin)
admin.site.register(Service)

def approve_applications(modeladmin, request, queryset):
    queryset.update(approved=True, rejected=False)
    for application in queryset:
        application.send_approval_email()

def reject_applications(modeladmin, request, queryset):
    queryset.update(rejected=True, approved=False)
    for application in queryset:
        application.send_rejection_email()

approve_applications.short_description = "Одобрить выбранные заявки"
reject_applications.short_description = "Отклонить выбранные заявки"

class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'service', 'appointment_date', 'appointment_time', 'approved', 'rejected')
    list_filter = ['approved', 'rejected', ('appointment_date', admin.DateFieldListFilter), 'appointment_time']
    search_fields = ['name', 'email', 'phone', 'tire_size',  'appointment_date', 'appointment_time']
    actions = [approve_applications, reject_applications]

admin.site.register(Application, ApplicationAdmin)

from django.contrib import admin
from django.core.mail import send_mail
from .models import Question

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'created_at', 'answered']
    list_filter = ['answered', 'created_at']
    search_fields = ['name', 'email', 'phone', 'question_text']

    def save_model(self, request, obj, form, change):
        if change and 'answer_text' in form.changed_data:
            obj.answered = True
            send_mail(
                'Ответ на ваш вопрос',
                obj.answer_text,
                'your_email@example.com',  # Отправитель
                [obj.email],  # Получатель
                fail_silently=False,
            )
        super().save_model(request, obj, form, change)
