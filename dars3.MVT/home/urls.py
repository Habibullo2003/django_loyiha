from django.urls import path
from .views import PostView, Post1View, Post2View

urlpatterns = [
    path('', PostView.as_view(), name='post'),
    path('about/', Post1View.as_view(), name='post1'),
    path('index/', Post2View.as_view(), name='post2')
]