from django.db import models


# Create your models here.
class Music(models.Model):
    title = models.CharField(null=False, max_length=255)
    link = models.TextField(null=True)
    authorName = models.CharField(null=True, max_length=255)
    producedAtDate = models.DateTimeField(null=True)
    createdAt = models.DateTimeField(null=False)
    updatedAt = models.DateTimeField(null=False)
