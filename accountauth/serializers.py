from django.contrib.auth.models import User
from .models import UserProfile

from rest_framework import serializers

class AuthUser(serializers.ModelSerializer) : 
    id = serializers.IntegerField(required=False)
    class Meta : 
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email')

class UserSerializer(serializers.ModelSerializer) : 
    user = AuthUser(many=False)
    class Meta : 
        model = UserProfile
        fields = (
            'id',
            'user',
            'profile_pic',
            'bio',
            'user'
        )
        
