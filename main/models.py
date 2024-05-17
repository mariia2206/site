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
