from __future__ import absolute_import, unicode_literals
import os

from celery import Celery

from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MyBlogSite.settings')

app = Celery('MyBlogSite')
app.conf.enable_utc = False

app.conf.update(timezone = 'Asia/Dhaka')

app.config_from_object('django.conf:settings', namespace='CELERY')


# DJANGO BEAT SETTING 

# app.conf.beat_schedule = {
#        'sendmail-task-crontab': {       
#         'task': 'send_email_periodic_task',
#         'schedule': crontab(hour=16, minute=0)
#         #'args': (16, 16),
#     },
       
#     'sendmail-every-5-seconds': {
#         'task': 'send_email_periodic_task',
#         'schedule': 5.0
#         #'args': (16, 16)
#     },
# }

@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")