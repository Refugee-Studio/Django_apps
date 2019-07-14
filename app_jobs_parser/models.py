from django.db import models

# Create your models here.

class Results(models.Model):
    Position = models.CharField(max_length=100)
    Company = models.CharField(max_length=100)
    Salary = models.CharField(max_length=100)
    URL = models.CharField(max_length=1000)
