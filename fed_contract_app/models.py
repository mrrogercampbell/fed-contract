from django.db import models

# Create your models here.

class Result(models.Model):
    title = models.CharField(max_length=200)
    headers = models.TextField()
    synopsis = models.TextField()
    naics = models.PositiveIntegerField()
    period = models.CharField(max_length=200)
    place = models.CharField(max_length=200)
    value = models.CharField(max_length=200)
    incumbent = models.TextField()
    matched = models.TextField()

    def __str__(self):
        return self.title


class Keyword(models.Model):
    keyword1 = models.CharField(max_length=200)
    keyword2 = models.CharField(max_length=200)
    keyword3 = models.CharField(max_length=200)
    keyword4 = models.CharField(max_length=200)
    keyword5 = models.CharField(max_length=200)
    keyword6 = models.CharField(max_length=200)

    def __str__(self):
    return self.title