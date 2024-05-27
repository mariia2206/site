from django.db import models
from django.core.mail import send_mail
from django.conf import settings


class Photo(models.Model):
    image = models.ImageField(upload_to='photos/')
    caption = models.CharField(max_length=255)

    def __str__(self):
        return self.caption

class Review(models.Model):
    author = models.CharField(max_length=100)
    review_text = models.TextField()
    photo = models.ImageField(upload_to='review_photos')

    def __str__(self):
        return self.author

class Action(models.Model):
    photo = models.ImageField(upload_to='action_photos/')
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.author

class Service(models.Model):
    name = models.TextField()
    photo = models.ImageField(upload_to='services_photos/')
    full_description = models.TextField()

    def __str__(self):
        return self.name

class Application(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    tire_size = models.CharField(max_length=50)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    appointment_date = models.DateField()
    appointment_time = models.CharField(max_length=10)
    comment = models.TextField()
    agreement = models.BooleanField(default=False)
    approved = models.BooleanField(default=False)
    rejected = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.service.name}"

    def send_approval_email(self):
        if self.approved and not self.rejected:
            subject = "Ваша заявка одобрена"
            message = (
                f"Здравствуйте, {self.name}.\n\n"
                f"Ваша заявка на услугу '{self.service.name}' была одобрена.\n"
                f"Дата записи: {self.appointment_date.strftime('%d-%m-%Y')}\n"
                f"Время записи: {self.appointment_time}\n\n"
                f"С уважением, ШинСервис Бтск-Дон."
            )
            send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [self.email])

    def send_rejection_email(self):
        if self.rejected:
            subject = "Ваша заявка отклонена"
            message = (
                f"Здравствуйте, {self.name}.\n\n"
                f"Ваша заявка на услугу '{self.service.name}' была отклонена.\n"
                f"Дата записи: {self.appointment_date.strftime('%d-%m-%Y')}\n"
                f"Время записи: {self.appointment_time}\n\n"
                f"С уважением, ШинСервис Бтск-Дон."
            )
            send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [self.email])

from django.db import models

class Question(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    question_text = models.TextField()
    agreement = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    answered = models.BooleanField(default=False)
    answer_text = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Question from {self.name} ({self.email})"
