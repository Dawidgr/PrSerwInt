from .models import Notification
from .serializers import NotificationSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET'])
def notification_list(request):
    try:
        user = request.user
        unread_notifications = Notification.objects.filter(user=user, is_read=False)
    except Notification.DoesNotExist:
        return Response({'detail': 'There is no unread notifications.'})

    if request.method == 'GET':
        serializer = NotificationSerializer(unread_notifications, many=True)
        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def notification_detail(request, id):
    try:
        notification = Notification.objects.get(id=id)
    except Notification.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = NotificationSerializer(notification)
        if not notification.is_read:
            notification.is_read = True
        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)


# Creating notifications
def create_notification_follow(user, follower):
    message = f"{follower.username} followed you."
    Notification.objects.create(user=user, message=message)


def create_notification_post(post):
    message = f"{post.user_added.username} added a new post: {post.title}"
    followers = post.user_added.followers.all()
    for follower in followers:
        Notification.objects.create(user=follower, message=message)


def create_notification_comment(user, post):
    message = f"{post.user_added.username} commented on your post: {post.title}"
    Notification.objects.create(user=user, message=message)


def create_notification_message(user, message_author):
    message = f"{message_author.username} messaged you."
    Notification.objects.create(user=user, message=message)
