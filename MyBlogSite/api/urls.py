from django.urls import path,include
from .views import (PostDetailApiView,PostListApiView,BlogCommentApiView,
                    PostListApi,PostDetailApi,CreateCommentapi,
                )
urlpatterns = [
path('', PostListApiView.as_view(), name='apipost_list'),
path('<str:slug>/',PostDetailApiView.as_view(), name='postdetail_api'),
path('<str:slug>/comment/',BlogCommentApiView.as_view(), name='comment_api'),
path('custom/comments/api',CreateCommentapi.as_view(), name='customcomment_api'),
path('ui/list/', PostListApi,name='apipostui_list'),
path('ui/list/<str:slug>/', PostDetailApi,name='apipostui_detail'),
path('api-auth/', include('rest_framework.urls')),
]