from rest_framework import serializers
from post import models
from community import serializers


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
    community = CommentSerializer(read_only=True)

    class Meta:
        model = models.Post
        fields = [
            'id',
            'community'
            'title',
            'description',
            'date_added',
            'user_added',
            'comments'
        ]