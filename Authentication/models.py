from django.db import models
from django.contrib.auth.models import AbstractUser

class RepeatFields(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    inactive = models.BooleanField(default=False)
    
class User(AbstractUser , RepeatFields):
    image = models.ImageField(upload_to="User_Image")