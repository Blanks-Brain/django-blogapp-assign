from django.urls import path,include
from .views import PostListView,PostDetailView,CreateNewPost,PostUpdateView,PostDeleteView

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('users/',include('users.urls')),
    path('new/',CreateNewPost, name='post_new'),
    path('<slug:slug>/update/',PostUpdateView.as_view(), name='post_update'),
    path('<slug:slug>/delete/',PostDeleteView.as_view(), name='post_delete'),
    path('<slug:slug>/',PostDetailView.as_view(), name='post_detail'),
   
]
