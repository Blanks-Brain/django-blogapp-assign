from rest_framework import serializers
from blog.models import Post,Comment

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        lookup_field = 'slug'
        fields = ['title','author','content','status','created_on','comments',]

class BlogCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model= Comment
        fields = ['id','author','text','post',]