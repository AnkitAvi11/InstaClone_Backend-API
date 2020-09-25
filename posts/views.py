from django.shortcuts import render

from .models import Post

from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import permission_classes, api_view, authentication_classes
from rest_framework.response import Response

from .serializers import PostSerializer

# Create your views here.
@api_view(['GET'])
def getPosts(request) : 
    posts = Post.objects.all()
    return Response (
        PostSerializer(posts, many=True).data,
        status=200
    )   