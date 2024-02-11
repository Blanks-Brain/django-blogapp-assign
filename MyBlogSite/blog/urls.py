from django.urls import path,include
from .views import (
    PostListView,PostDetailView,CreateNewPost,
   PostUpdateView,PostDeleteView,DraftPostListView,
   PostPublishView,AddCommentView,
)
urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('accounts/',include('accounts.urls')),
    path('new/',CreateNewPost, name='post_new'),
    path('<slug:slug>/update/',PostUpdateView.as_view(), name='post_update'),
    path('<slug:slug>/delete/',PostDeleteView.as_view(), name='post_delete'),
    path('<slug:slug>/comment/',AddCommentView, name='post_comment'),
    path('draft/',DraftPostListView.as_view(), name='draftpost'),
    path('draft/<slug:slug>/publish/',PostPublishView.as_view(), name='post_publish'),
    path('<slug:slug>/',PostDetailView.as_view(), name='post_detail'),
   
]
