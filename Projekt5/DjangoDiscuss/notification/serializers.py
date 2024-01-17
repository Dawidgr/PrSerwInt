from rest_framework import serializers
from . import models


class NotificationSerializer(serializers.ModelSerializer):
    timestamp = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = models.Notification
        fields = [
            'id',
            'user',
            'message',
            'timestamp',
            'is_read'
        ]
