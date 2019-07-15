from django.db import models

# Create your models here.

class Results(models.Model):
    Position = models.CharField(max_length=100, unique=False)
    Company = models.CharField(max_length=100, unique=False)
    Salary = models.CharField(max_length=100, unique=False)
    URL = models.CharField(max_length=1000, unique=True)
