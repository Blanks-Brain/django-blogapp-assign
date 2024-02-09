from django.shortcuts import render,redirect
from .forms import CustomUserCreationForm,CustomAuthenticationForm
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def SignUp(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})

# def LogIn(request):
#     if request.method == "POST":
#         print("Yes1")
#         form = CustomAuthenticationForm(request.POST)
#         if form.is_valid():
#             print("yes2")
#             return redirect('home')
#     else:
#         form = CustomAuthenticationForm()
#     return render(request, 'login.html', {'form': form})
   