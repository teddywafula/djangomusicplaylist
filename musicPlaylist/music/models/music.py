from django.db import models


# Create your models here.
class Music(models.Model):
    title = models.CharField(null=False, max_length=255, blank=False)
    link = models.TextField(null=True, blank=True)
    authorName = models.CharField(null=True, max_length=255, blank=True)
    producedAtDate = models.DateTimeField(null=True, blank=True)
    createdAt = models.DateTimeField(null=False)
    updatedAt = models.DateTimeField(null=False)
    slug = models.SlugField(default="", null=False)