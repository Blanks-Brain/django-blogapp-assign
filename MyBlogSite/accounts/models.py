from django.db import models
from .manager import CustomUserManager
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    username = models.CharField(max_length = 50, blank = True, null = True, unique = True)
    email = models.EmailField(unique=True,blank=True,null=True)
    is_active = models.BooleanField(default = False)
    otp = models.CharField(max_length = 6, blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    objects = CustomUserManager()
     
