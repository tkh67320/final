from django.db import models

# Create your models here.

class AgHill(models.Model):
    stop = models.CharField(max_length=50)
    time = models.Time()

