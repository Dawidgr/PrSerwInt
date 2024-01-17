from rest_framework import serializers
from . import models


class MessageSerializer(serializers.ModelSerializer):
    datetime_sent = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = models.Message
        fields = [
            'id',
            'sender',
            'receiver',
            'datetime_sent',
            'content'
        ]
