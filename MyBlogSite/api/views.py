from django.shortcuts import render
from blog.models import Post
from rest_framework import generics
from .serializers import PostSerializer
# Create your views here.


class PostListApiView(generics.ListCreateAPIView):
   queryset = Post.objects.filter(status=1).order_by('-created_on')
   serializer_class = PostSerializer

class PostDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'