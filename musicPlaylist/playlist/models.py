from django.db import models


# Create your models here.


class Playlist(models.Model):
    PRIVACY_CHOICES = [
        ('PR', 'Private'),
        ('UL', 'Unlisted'),
        ('PU', 'Public'),
    ]
    name = models.CharField(max_length=100)
    privacy = models.CharField(max_length=2, choices=PRIVACY_CHOICES, default='PR', null=False)
