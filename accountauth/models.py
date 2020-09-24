from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class UserProfile (models.Model) : 
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='images/%Y/%m/', default='default.png')
    bio = models.TextField(null=True, blank=True)

    def __str__(self) : 
        return self.user.username

def createUserProfile(sender, **kwargs) : 
    if kwargs['created'] : 
        UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(createUserProfile, sender=User)
