from rest_framework import serializers
from post import models
from community.models import Community


class CommentSerializer(serializers.ModelSerializer):
    date_added = serializers.DateField(read_only=True, format='%d %B %Y')

    class Meta:
        model = models.Comment
        fields = [
            'id',
            'content',
            'date_added',
            'user_added',
            'post',
        ]


class PostSerializer(serializers.ModelSerializer):
    date_added = serializers.DateField(read_only=True, format='%d %B %Y')
    comments = CommentSerializer(read_only=True, many=True, source='comment_set')
    in_community = serializers.PrimaryKeyRelatedField(queryset=Community.objects.all())

    class Meta:
        model = models.Post
        fields = [
            'id',
            'title',
            'description',
            'date_added',
            'user_added',
            'in_community',
            'is_moderated',
            'comments'
        ]
