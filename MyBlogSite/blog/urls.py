from django.urls import path,include
from .views import PostListView,PostDetailView,CreateNewPost

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('users/',include('users.urls')),
    path('new/',CreateNewPost, name='post_new'),
    path('<slug:slug>/',PostDetailView.as_view(), name='post_detail'),
    
]
