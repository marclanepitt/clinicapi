from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name="user_profile", on_delete=models.CASCADE)
    phone = models.CharField(max_length = 12)

    def __str__(self):
        return '{} {}'.format(self.user.first_name, self.user.last_name)

class ClinicAdmin(models.Model):
    user = models.OneToOneField(User, related_name="clinic_admin", on_delete=models.CASCADE)