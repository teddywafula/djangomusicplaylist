from django.db import models

# Create your models here.

class Person(models.Model):
    GenderType = models.TextChoices('GenderType', 'MALE FEMALE')
    first_name = models.CharField(max_length=100, null=False)
    surname = models.CharField(max_length=100, null=False)
    middle_name = models.CharField(max_length=100, null=True)
    birth_date = models.DateField(null=True)
    gender = models.CharField(blank=True, choices=GenderType.choices, max_length=10)