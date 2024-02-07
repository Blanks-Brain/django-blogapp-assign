from django.shortcuts import render,redirect
from .models import Post
from django.views.generic import ListView,DeleteView
from django.views.generic import CreateView
from .forms import PostForm
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your views here.


def CreateNewPost(request):
    if request.method == "POST":
        form= PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', slug= post.slug)
    else:
        form = PostForm()
    return render(request, 'post_new.html', {'form': form})


class PostListView(ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    
    template_name= 'index.html'

class PostDetailView(DeleteView):
    model = Post
    template_name ='post_detail.html'