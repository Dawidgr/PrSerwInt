from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class CustomUser(AbstractUser):
    followers = models.ManyToManyField(to=settings.AUTH_USER_MODEL, symmetrical=False, blank=True)
    
    def __str__(self):
        return f"{self.id}: {self.username}"
