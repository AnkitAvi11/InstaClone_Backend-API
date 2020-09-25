from django.db import models

from django.contrib.auth.models import User
from datetime import datetime

class Post(models.Model) : 
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_foreign")
    title = models.CharField(max_length = 300)
    image = models.ImageField(upload_to = "images/%Y/%m/")
    date_posted = models.DateTimeField(default=datetime.now())
    likes = models.ManyToManyField(User, related_name='user_likes')

    def __str__(self) : 
        return self.title

    def delete(self, *arga, **kwargs) : 
        pass


class Comment(models.Model) : 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length = 300)

    def __str__(self) : 
        return self.user.username 
