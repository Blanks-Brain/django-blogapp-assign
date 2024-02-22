from celery import shared_task
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from MyBlogSite import settings

@shared_task(bind = True)

def send_mail_func(self):
    users = get_user_model().objects.all()
    for user in users:
        mail_subject = "Hi! Celery Testing"
        message = "I hope all of are you well.Thank for comming today"
        to_email = user.email
        send_mail(
            subject=mail_subject,
            message= message,
            from_email= settings.EMAIL_HOST_USER,
            recipient_list=[to_email],
            fail_silently= True,
            
        )
    return "Done"