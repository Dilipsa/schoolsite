from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    mobile = models.CharField(max_length=10, null=True, blank=True)
    profile_pic = models.ImageField(upload_to="profile_pictures", null=True, blank=True)