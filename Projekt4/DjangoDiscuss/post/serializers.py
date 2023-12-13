from rest_framework import serializers
from post import models


class CommentSerializer(serializers.ModelSerializer):
    date_added = serializers.DateField(read_only=True, format='%d %B %Y')

    class Meta:
        model = models.Comment
        fields = [
            'id',
            'content',
            'date_added',
            'user_added',
            'post'
        ]


class PostSerializer(serializers.ModelSerializer):
    date_added = serializers.DateField(read_only=True, format='%d %B %Y')
    comments = CommentSerializer(read_only=True, many=True, source='comment_set')

    class Meta:
        model = models.Post
        fields = [
            'id',
            'title',
            'description',
            'date_added',
            'user_added',
            'comments'
        ]

