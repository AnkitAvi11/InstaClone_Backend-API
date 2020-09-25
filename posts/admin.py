from django.contrib import admin

# Register your models here.
from .models import Post

class PostAdmin(admin.ModelAdmin) : 
    list_display = ('id', 'user', 'title')
    list_display_links = ('id', 'user', 'title')


admin.site.register(Post)