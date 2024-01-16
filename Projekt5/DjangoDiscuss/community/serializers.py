from rest_framework import serializers
from community import models


class CommunitySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Community
        fields = [
            'id',
            'name',
            'description',
            'ownership',
            'members'
        ]
