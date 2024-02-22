from django.shortcuts import render
from .tasks import send_mail_func
# Create your views here.
from django.http import HttpResponse

def send_mail_all(request):
    send_mail_func.delay()
    return HttpResponse("sent")
    