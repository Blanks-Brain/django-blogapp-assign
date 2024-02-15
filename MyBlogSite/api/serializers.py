from rest_framework import serializers
from blog.models import Post,Comment

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title','author','slug','content','status','created_on',)

class BlogCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model= Comment
        fields = '__all__'