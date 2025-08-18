from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phonenumber = models.CharField(max_length=20)
    kakaotalkID = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=20, blank=True, null=True, default="")
    academicyear = models.CharField(max_length=20, blank=True, null=True, default="")
    intendedmajor = models.CharField(max_length=50, blank=True, null=True, default="")

    def __str__(self):
        return self.user.username