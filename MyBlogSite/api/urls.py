from django.urls import path
from .views import PostDetailApiView,PostListApiView

urlpatterns = [
path('', PostListApiView.as_view()),
path('<str:slug>/',PostDetailApiView.as_view()),

]