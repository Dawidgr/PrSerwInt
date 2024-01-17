from rest_framework import serializers
from django.contrib.auth import get_user_model


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [
            'id',
            'username',
            'followers'
        ]


class FollowUserSerializer(serializers.Serializer):
    follower = serializers.PrimaryKeyRelatedField(queryset=get_user_model().objects.all())
