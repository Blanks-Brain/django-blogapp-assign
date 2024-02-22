from django.urls import path 
from .views import send_mail_all

urlpatterns = [
    path('',send_mail_all,name="sendmail"),
]