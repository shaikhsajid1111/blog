from django.shortcuts import render
from django.contrib import admin
from django.views.generic import ListView,DetailView
from . models import Post
# Create your views here.
class PostList(ListView):
    queryset = Post.objects.filter(status = 1).order_by('-created_on')
    template_name = 'index.html'
class PostDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'
