from statistics import mode
from django.db import models

# Create your models here.
class MovieData(models.Model):
    title = models.CharField(max_length=100)
    rating = models.CharField(max_length=20)
    relase_date = models.CharField(max_length=10)
    description = models.TextField()

    def __str__(self):
        return self.title + self.rating