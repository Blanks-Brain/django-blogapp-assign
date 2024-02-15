from django.urls import path,include
from .views import PostDetailApiView,PostListApiView,PostListApi,PostDetailApi
urlpatterns = [
path('list/', PostListApiView.as_view(), name='apipost_list'),
path('list/<str:slug>/',PostDetailApiView.as_view(), name='postdetail_api'),
path('ui/list/', PostListApi,name='apipostui_list'),
path('ui/list/<str:slug>/', PostDetailApi,name='apipostui_detail'),
path('api-auth/', include('rest_framework.urls')),
]