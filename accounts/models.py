from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(max_length=255, blank=True, null=True)
    age = models.PositiveSmallIntegerField(blank=True, null=True)
    description = models.TextField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=124, blank=True, null=True, verbose_name="Email Address")
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)

    def __str__(self) -> str:
        return ''
