from django.shortcuts import render,redirect,get_object_or_404
from .models import Post,Comment
from django.views.generic import ListView,DetailView,UpdateView,DeleteView,CreateView
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

def AddCommentView(request,slug):
    post = Post.objects.get(slug=slug)
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.author = request.user
            
            new_comment.save()
            return redirect('post_detail', slug= post.slug)
    else:
        comment_form = CommentForm()
    return render(request, 'post_comment.html',{'comment_form': comment_form} )

    
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
    
# class PostDetailView(DetailView):
#     model = Post
#     template_name ='post_detail.html'

def PostDetailView(request, slug):
    template_name = 'post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.all()
    return render(request, template_name, {'post': post,'comments': comments,})
    
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')
