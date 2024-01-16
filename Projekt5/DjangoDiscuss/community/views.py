from .models import Community
from .serializers import CommunitySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def community_list(request):
    if request.method == 'GET':
        communities = Community.objects.all()
        serializer = CommunitySerializer(communities, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = CommunitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE'])
def community_detail(request, id):
    try:
        community = Community.objects.get(pk=id)
    except Community.DoesNotExist:
        return Resposne(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CommunitySerializer(community)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CommunitySerializer(community, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE':
        community.delete()
        return Resposne(status=status.HTTP_204_NO_CONTENT)
