# models.py
from django.db import models

class Timer(models.Model):
    name = models.CharField(max_length=100)
    elapsed_time = models.IntegerField(default=0)
