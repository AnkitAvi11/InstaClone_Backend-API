from django.shortcuts import render
from .models import UserProfile
from django.contrib.auth import authenticate, login

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
    

@api_view(['POST'])
def loginUser(request) : 
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(username=username, password=password)

    if user is not None : 
        token, created = Token.objects.get_or_create(
            user=user
        )
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
