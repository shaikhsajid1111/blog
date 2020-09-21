from django.shortcuts import render,redirect
from django.contrib import admin
from django.views.generic import ListView,DetailView
from . models import Post
from django.utils.datastructures import MultiValueDictKeyError
# Create your views here.
class PostList(ListView):
    queryset = Post.objects.filter(status = 1).order_by('-created_on')
    template_name = 'index.html'
class PostDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'


def search(request):
    query = request.GET['query']
    if query != "":
        return render(request,"search.html",{"post_list": Post.objects.filter(title__icontains = query)})        
    else:
        return redirect("/")