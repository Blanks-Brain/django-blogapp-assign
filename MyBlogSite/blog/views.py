from django.shortcuts import render,redirect,get_object_or_404
from .models import Post,Comment
from django.views.generic import ListView,DetailView,UpdateView,DeleteView
from .forms import PostForm,CommentForm
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
User = get_user_model()
# Create your views here.


def CreateNewPost(request):
    if request.method == "POST":
        form= PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            if post.status == 0: # for DraftPost List
               return redirect('draftpost')
           
            return redirect('post_detail', slug= post.slug)
    else:
        form = PostForm()
    return render(request, 'post_new.html', {'form': form})

def AddCommentView(request):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.email=request.email
            form.save()
            return redirect('post_detail', slug= post.slug)
        else:
            form = CommentForm()
    return render(request, 'post_comment.html', {'form': form})

class PostUpdateView(UpdateView):
    model = Post
    template_name = "post_update.html"
    fields = ['title','content','status']
    
class PostPublishView(UpdateView):
    model = Post
    template_name = "post_publish.html" 
    fields = ['status']
       
class PostListView(ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name= 'index.html'

class DraftPostListView(ListView):
    queryset = Post.objects.filter(status=0).order_by('-created_on')
    template_name = "draftPost_list.html"
    
class PostDetailView(DetailView):
    model = Post
    template_name ='post_detail.html'
    
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')
    