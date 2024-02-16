from django.contrib import admin
from .models import CustomUser 
# Register your models here.

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id','username','email','is_verified','otp')

admin.site.register(CustomUser)

