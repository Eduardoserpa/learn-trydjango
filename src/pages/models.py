# Create your models here.
from django.db import models

class Page(models.Model):
    description = models.CharField(max_length=500)

    def __str__(self):
        # Admin refers to the object by its 'title' attribute
        return self.title