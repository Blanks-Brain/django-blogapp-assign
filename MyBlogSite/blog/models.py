from django.urls import reverse
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from django.utils import timezone

User = get_user_model()
# Create your models here.

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length = 200 , unique = True)
    slug = models.SlugField(max_length=200, unique=True,null=False)
    author = models.ForeignKey(User, on_delete = models.CASCADE ,related_name='blog_posts')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now= True)
    status = models.IntegerField(choices = STATUS, default = 0)
    
    class Meta:
        ordering = ['-created_on']
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):  # for slug
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"slug": self.slug})

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete = models.CASCADE, related_name = 'comments')
    author = models.TextField(default = False)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    
    
    class Meta:
        ordering = ['created_date']
    
   