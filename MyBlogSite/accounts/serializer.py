from rest_framework import serializers
from .models import CustomUser

class UserlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields=('id','username','email',)

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username','email','password','is_active',]

class VerifyAccountSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField()

    