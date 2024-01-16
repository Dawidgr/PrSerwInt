from django.db import models
from django.contrib.auth.models import User
from community.models import Community
from django.conf import settings


class Post(models.Model):
    title = models.CharField(max_length=300)
    description = models.CharField(max_length=10000)
    date_added = models.DateField(auto_now=True)
    user_added = models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    in_community = models.ForeignKey(Community, on_delete=models.CASCADE)


    def __str__(self):
        return self.title


class Comment(models.Model):
    content = models.TextField(max_length=10000)
    date_added = models.DateField(auto_now=True)
    user_added = models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"Comment by {self.user_added.username} on {self.post.title}"
