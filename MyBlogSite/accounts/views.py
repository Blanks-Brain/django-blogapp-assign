from django.shortcuts import render,redirect
from django.contrib.auth import views as auth_views
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.views.generic import View
from .forms import CustomLoginForm,CustomRegisterForm
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