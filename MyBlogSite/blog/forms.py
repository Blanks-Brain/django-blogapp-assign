from django import forms

from .models import Post,Comment
from .tasks import send_Comment_email_task
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content","status"]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["text"]
        
    # def send_email(request):
    #     send_Comment_email_task.delay()    