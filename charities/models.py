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


class TaskManager(models.Manager):
    def related_tasks_to_charity(self, user):
        try:
            charity = Charity.objects.get(user=user)
            return self.filter(charity=charity)
        except Charity.DoesNotExist:
            return self.none()

    def related_tasks_to_benefactor(self, user):
        try:
            benefactor = Benefactor.objects.get(user=user)
            return self.filter(assigned_benefactor=benefactor)
        except Benefactor.DoesNotExist:
            return self.none()

    def all_related_tasks_to_user(self, user):
        try:
            benefactor = Benefactor.objects.get(user=user)
            charity = Charity.objects.get(user=user)

            tasks_as_benefactor = self.filter(assigned_benefactor=benefactor)
            tasks_as_charity = self.filter(charity=charity)
            pending_tasks = self.filter(state='P')

            return (tasks_as_benefactor | tasks_as_charity | pending_tasks).distinct()
        except (Benefactor.DoesNotExist, Charity.DoesNotExist):
            return self.filter(state='P')

class Task(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    STATE_CHOICES = [
        ('P', 'Pending'),
        ('W', 'Waiting'),
        ('A', 'Assigned'),
        ('D', 'Done'),
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

    objects = TaskManager()
