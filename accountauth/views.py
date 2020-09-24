from django.shortcuts import render
from .models import UserProfile
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework.authtoken.models import Token
from rest_framework import status

@api_view(['GET'])
def getUser(request) : 
    users = UserProfile.objects.all()
    return Response(
        UserSerializer(users, many=True).data
    )
    
#   login api for the user
@api_view(['POST'])
def loginUser(request) : 
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(username=username, password=password)

    if user is not None : 
        login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            "token" : token.key,
            "auth" : UserSerializer(user.userprofile, many=False).data
        })
    else : 
        return Response(
        {
            "status" : "Error",
            "message" : "Invalid username or password. Authentication Failed"
        },
        status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION
        )

#   signup api for the user
@api_view(['POST'])
def signupUser (request) : 
    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')

    
    user = User.objects.create_user(username=username, email=email, password=password)
    return Response(
        UserSerializer(user.userprofile, many=False).data,
        status=status.HTTP_201_CREATED
    )
