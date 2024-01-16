from rest_framework import serializers
from django.contrib.auth import get_user_model


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [
            'id',
            'username',
            'followed_users'
        ]


class FollowUserSerializer(serializers.Serializer):
    user_to_follow = serializers.PrimaryKeyRelatedField(queryset=get_user_model().objects.all())
