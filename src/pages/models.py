from django.db import models

# Create your models here.
class Page(models.Model):
    description = models.CharField(max_length=500)