from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Post

#   user serializer to get only the important user details
class UserSerializer(serializers.ModelSerializer) : 
    id = serializers.IntegerField(required=False)
    
    class Meta : 
        model = User
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'username'
        )

#   Post Serializer to get the relevant post details
class PostSerializer(serializers.ModelSerializer) : 

    user = UserSerializer(many=False)

    class Meta : 
        model = Post
        fields = (
            'id',
            'title',
            'image',
            'date_posted',
            'user',
            'likes'
        )
        depth = 1

