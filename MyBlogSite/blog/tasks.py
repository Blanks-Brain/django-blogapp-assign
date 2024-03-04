from time import sleep
from celery import shared_task
from django.core.mail import send_mail
from MyBlogSite import settings
from django.contrib.auth import get_user_model
from django_celery_beat.models import PeriodicTask, IntervalSchedule
import json
from .models import Post
from datetime import date

today = date.today()


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


@shared_task
def send_email_periodic_task(key):
    posts = Post.objects.filter(today_date=today)
    allpost=""
    for post in posts:
        allpost+=str(post.title)+' , '
    
    users = get_user_model().objects.all()
    mail_subject = "New Post Notification"
    message = "Today new  Post list "+allpost

    for user in users:
        send_mail(
            subject=mail_subject,
            message= message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user],
            fail_silently= True,    
            )
    print(f"Email Periodic key: {key}")
    return key

# Create Schedule every 10 seconds
schedule, created = IntervalSchedule.objects.get_or_create(
    every=10,
    period=IntervalSchedule.SECONDS,
)
PeriodicTask.objects.get_or_create(
    name='Send Email Periodic Task',
    task='blog.tasks.send_email_periodic_task',
    interval=schedule,
    args=json.dumps(['hello']),  # Pass the arguments to the task as a JSON-encoded list
)
    
