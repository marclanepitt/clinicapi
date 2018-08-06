from django.db import models
from apps.users.models import StaffUser

class Sport(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Clinic(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    organizer = models.ForeignKey(StaffUser, on_delete=models.CASCADE)
    image = models.ImageField(null=True)
    county = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Event(models.Model):
    datetime = models.DateTimeField()
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    price = models.IntegerField()
    location = models.CharField(max_length=1000)
    rating = models.IntegerField()
    age_range = models.CharField(max_length=12)
    SKILL_CHOICES = (
        ('ALL', 'ALL'),
        ('BEG', 'Beginner'),
        ('MID', 'Mid Level'),
        ('HGH', 'High Level')
    )
    skill_level = models.CharField(
        max_length=3,
        choices=SKILL_CHOICES,
        default='ALL'
    )
    def __str__(self):
        return self.name
