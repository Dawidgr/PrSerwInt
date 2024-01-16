from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class CustomUser(AbstractUser):
    followed_users = models.ManyToManyField(to=settings.AUTH_USER_MODEL, symmetrical=False, related_name='follows', blank=True)
    
    def __str__(self):
        return self.username
