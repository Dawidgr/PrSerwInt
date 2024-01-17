from .models import CustomUser
from .serializers import CustomUserSerializer, FollowUserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from notification.views import create_notification_follow


@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, id):
    try:
        user = CustomUser.objects.get(pk=id)
    except CustomUser.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CustomUserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['PUT'])
def user_follow(request, id):
    try:
        user = CustomUser.objects.get(pk=id)
    except CustomUser.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = FollowUserSerializer(data=request.data)
    if request.method == 'PUT':
        if serializer.is_valid():
            follower = serializer.validated_data['follower']
            if follower in user.followers.all():
                user.followers.remove(follower)
            else:
                user.followers.add(follower)
                create_notification_follow(user=user, follower=follower)
            return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
