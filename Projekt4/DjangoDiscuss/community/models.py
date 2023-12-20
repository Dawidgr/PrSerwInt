from django.db import models
from django.contrib.auth.models import User
from post.models import Post


class Community(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=10000)
    ownership = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    members = models.ManyToManyField(Post, blank=True, related_name='subscribed_communities')

    def __str__(self):
        return self.name
