from time import sleep
from celery import shared_task
from django.core.mail import send_mail
from MyBlogSite import settings
from django.contrib.auth import get_user_model

@shared_task(bind = True)
def send_Comment_email_task(self,message):
    nl="\n"
    mail_subject = "Hi! comment"
    messages = f"User {message[1]} {nl}New Comment is :  {message[0]}."
    to_email = message[2]
    send_mail(
        subject=mail_subject,
        message= messages,
        from_email= settings.EMAIL_HOST_USER,
        recipient_list=[to_email],
        fail_silently= True,    
        )
    return "Done"