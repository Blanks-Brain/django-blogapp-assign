from django.shortcuts import render,redirect
from django.contrib.auth import views as auth_views
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.views.generic import View
from .forms import CustomRegisterForm,CustomLoginForm
from django.contrib.auth import logout


# Create your views here.


class SignupView(CreateView):
    form_class = CustomRegisterForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')

class LoginView(auth_views.LoginView):
    form_class = CustomLoginForm
    template_name = 'login.html'
    success_url = reverse_lazy('home')

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('home')
    
# Create Api Accounts 

from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import CustomUserSerializer,VerifyAccountSerializer
from .email import send_otp_via_email
from .models import CustomUser


class CustomUserSignupApi(APIView):
    
    def post(self, request):
        try:
            data = request.data 
            serializer = CustomUserSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                send_otp_via_email(serializer.data['email'])
                return Response({
                    'status': 200,
                    'message': 'registration successfully check email',
                    'data': serializer.data,                  
                })
            
            return Response({
                'status': 400,
                'message':'Something is wrong',
                'data': serializer.errors
            })
        except Exception as e:
            print(e)

class VerifyOtp(APIView):
    def post(self,request):
        try:
            data = request.data
            print(data)
            serializer = VerifyAccountSerializer(data=data)
            print(serializer)
            if serializer.is_valid():
               email = serializer['email']
               otp = serializer['otp']
               user = CustomUser.objects.filter(email = email)
               
               print(user)
               print(email,otp)
               if not user.exists():
                    return Response({
                    'status': 400,
                    'message':'Something is wrong',
                    'data': 'invalid user'
                    })
              
               if user[0].otp!= otp:
                    return Response({
                    'status': 400,
                    'message':'Something is wrong',
                    'data': 'wrong otp'
                    })
                
               user = user.first()    
               user.is_active=True
               user.save()
                       
        except Exception as e:
            print(e)
        