from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(null=False, max_length=255, blank=False, unique=True)