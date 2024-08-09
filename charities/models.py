from django.db import models
from accounts.models import User


class Benefactor(models.Model):
    EXPERIENCE_LEVELS = [
        (0, 'Beginner'),
        (1, 'Intermediate'),
        (2, 'Expert'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    experience = models.SmallIntegerField(choices=EXPERIENCE_LEVELS, default=0)
    free_time_per_week = models.PositiveSmallIntegerField(default=0)


class Charity(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    reg_number = models.CharField(max_length=10)


class Task(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    STATE_CHOICES = [
        ('P', 'Pending'),  # در انتظار برای درخواست انجام فعالیت توسط نیکوکار
        ('W', 'Waiting'),  # در انتظار برای تایید درخواست توسط خیریه
        ('A', 'Assigned'),  # فعالیت به یک نیکوکار اختصاص داده شده
        ('D', 'Done'),      # به اتمام رسیدن فعالیت
    ]

    assigned_benefactor = models.ForeignKey(Benefactor, blank=True, null=True, on_delete=models.SET_NULL)
    charity = models.ForeignKey(Charity, on_delete=models.CASCADE)
    age_limit_from = models.IntegerField(blank=True, null=True)
    age_limit_to = models.IntegerField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    gender_limit = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)
    state = models.CharField(max_length=1, choices=STATE_CHOICES, default='P')
    title = models.CharField(max_length=60)
