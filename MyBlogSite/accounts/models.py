from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# Create your models here.

class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'), unique = True)
    is_verified = models.BooleanField(default = False)
    otp = models.CharField(max_length=6, null=True, blank=True)  # Add the otp field he