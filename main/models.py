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
    photo2 = models.ImageField(upload_to='action_photos/')
    author2 = models.CharField(max_length=100)

    def __str__(self):
        return self.author2

class Service(models.Model):
    name = models.CharField(max_length=200)
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
            message = "Здравствуйте, Ваша заявка на услугу была одобрена."
            send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [self.email])

    def send_rejection_email(self):
        if self.rejected:
            subject = "Ваша заявка отклонена"
            message = "Здравствуйте, Ваша заявка на услугу была отклонена."
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
