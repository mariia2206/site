# Create your models here.
from django.db import models
# Класс для галереи
class Photo(models.Model):
    image = models.ImageField(upload_to='photos/')
    caption = models.CharField(max_length=255)

    def __str__(self):
        return self.caption

# Класс поиска
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()


class Review(models.Model):
    author = models.CharField(max_length=100)
    review_text = models.TextField()
    photo = models.ImageField(upload_to='review_photos')

    def __str__(self):
        return self.author

