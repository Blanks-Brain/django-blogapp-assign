from django.urls import path
from .views import SignUp #,LogIn
urlpatterns = [
    path('signup/',SignUp, name='signup'), 
    # path('login/',LogIn, name='login'), 
      
]
