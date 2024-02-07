from django.shortcuts import render,redirect
from .forms import CustomUserCreationForm
# Create your views here.

def SignUp(request):
    if request.method == "POST":
        print("Yes1")
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            print("Yes2")
            form.save()
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})
