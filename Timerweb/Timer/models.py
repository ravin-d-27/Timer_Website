from django.db import models

class Timer(models.Model):
    name = models.CharField(max_length=100)
    
