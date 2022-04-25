from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile= models.ForeignKey('users.Profile', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='post/photos')
    created= models.DateTimeField(auto_now_add=True)
    created= models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        # return tittle and username
        return '{} br @{}'.format(self.title, self.user.username)