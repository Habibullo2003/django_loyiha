from django.shortcuts import render
from django.views.generic import ListView
from .models import Post,Post1,Post2
# Create your views here.

class PostView(ListView):
    model = Post
    template_name = 'home.html'
class Post1View(ListView):
    model = Post1
    template_name = 'about.html'
class Post2View(ListView):
    model = Post2
    template_name = 'index.html'