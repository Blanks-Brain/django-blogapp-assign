from django.urls import path
from .views import SignupView,LoginView,LogoutView,CustomUserSignupApi,VerifyOtp
urlpatterns = [
    path('signup/',SignupView.as_view(), name='signup'), 
    path('login/',LoginView.as_view(), name='login'), 
    path('logout/',LogoutView.as_view(), name='logout'), 
    
    # Api endpoints for accounts
    path('signupapi/',CustomUserSignupApi.as_view(), name='signupapi'),
    path('verifyotp/',VerifyOtp.as_view(), name='verifyotp'),
    
]
