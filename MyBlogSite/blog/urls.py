from django.urls import path
from .views import PostListView,PostDetailView,CreateNewPost
urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('new/',CreateNewPost, name='post_new'),
    path('<slug:slug>/',PostDetailView.as_view(), name='post_detail'),
    
]
