from django.shortcuts import render
from blog.models import Post
from rest_framework import generics
from .serializers import PostSerializer
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
import requests
# Create your views here.


class PostListApiView(generics.ListCreateAPIView):
   queryset = Post.objects.filter(status=1).order_by('-created_on')
   serializer_class = PostSerializer
   lookup_field = 'slug'
   
class PostDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'
  
def PostListApi(request):
    response = requests.get('http://127.0.0.1:8000/api/v1/list/')
    posts = response.json()
    return render(request, 'blogapi/api_post_list.html', {'posts': posts})
    
    
def PostDetailApi(request,slug):
    response = requests.get('http://127.0.0.1:8000/api/v1/list/<str:slug>')
    post = response.json()
    return render(request, 'blogapi/apipost_detail.html', {'post': post})