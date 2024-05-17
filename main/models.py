# Create your models here.
from django.db import models
# Класс для галереи
class Photo(models.Model):
    image = models.ImageField(upload_to='photos/')
    caption = models.CharField(max_length=255)

    def __str__(self):
        return self.caption

# Класс для отзывов
class Review(models.Model):
    author = models.CharField(max_length=100)
    review_text = models.TextField()
    photo = models.ImageField(upload_to='review_photos')

    def __str__(self):
        return self.author

class Action(models.Model):
    photo2 = models.ImageField(upload_to='action_photos/')
    author2 = models.CharField(max_length=100)

    def __str__(self):
        return self.author2


class Service(models.Model):
    name = models.CharField(max_length=200)
    full_description = models.TextField()
    photo = models.ImageField(upload_to='services_photos/')

    def __str__(self):
        return self.name

# models.py
from django.db import models
from django.core.mail import send_mail
from django.conf import settings

class Application(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    tire_size = models.CharField(max_length=50)
    service = models.CharField(max_length=100)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    comment = models.TextField()
    agreement = models.BooleanField(default=False)
    approved = models.BooleanField(default=False)
    rejected = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def send_approval_email(self):
        if self.approved and not self.rejected:
            subject = "Ваша заявка одобрена"
            message = "Здравствуйте, Ваша заявка на услугу была одобрена."
            send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [self.email])

    def send_rejection_email(self):
        if self.rejected:
            subject = "Ваша заявка отклонена"
            message = "Здравствуйте, Ваша заявка на услугу была отклонена."
            send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [self.email])
