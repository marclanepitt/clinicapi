from django.db import models
from apps.users.models import UserProfile

class Sport(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=100)

class Clinic(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    staff = models.ManyToManyField(UserProfile)

class Event(models.Model):
    date = models.DateTimeField()
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)