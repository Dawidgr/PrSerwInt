from django.db import models
from django.conf import settings


class Community(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=10000)
    ownership = models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    members = models.ManyToManyField(to=settings.AUTH_USER_MODEL, blank=True, related_name='subscribed_communities')

    class Meta:
        verbose_name_plural = 'Communities'

    def __str__(self):
        return f"{self.id}: {self.name}"
