from django.db import models
from django.conf import settings


class Message(models.Model):
    sender = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='sent_message')
    receiver = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='received_message')
    datetime_sent = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=2000)

    def __str__(self):
        return f"{self.id}: From {self.sender} to {self.receiver}"
