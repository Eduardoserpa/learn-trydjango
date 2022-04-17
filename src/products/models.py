from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10000)
    summary = models.TextField(default='Write here a summary of what the product is about.')

    def __str__(self):
        # Admin refers to the object by its 'title' attribute
        return self.title