# Create your models here.
from django.db import models

class Photo(models.Model):
    image = models.ImageField(upload_to='photos/')
    caption = models.CharField(max_length=100)

    def __str__(self):
        return self.caption
