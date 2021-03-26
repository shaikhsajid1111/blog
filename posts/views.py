from django.shortcuts import render,redirect,HttpResponseRedirect,HttpResponse,get_object_or_404
from django.contrib import admin
from django.views.generic import ListView,DetailView
from . models import Post,Comment
from django.utils.datastructures import MultiValueDictKeyError
# Create your views here.
class PostList(ListView):
    queryset = Post.objects.filter(status = 1).order_by('-created_on')
    template_name = 'index.html'
class PostDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'


def delete_comment(request):
    return HttpResponse("delete Comment!")

def post_comment(request,pk):

    if request.method == "POST":
        text = request.POST.get('comment')
        user = request.user
        post = get_object_or_404(Post,pk=pk)
        
        if text != "" and text is not None:
            comment = Comment()
            comment.author = user
            comment.text = text
            comment.post = post
            comment.save()
            return HttpResponseRedirect(request.__dict__['environ']['HTTP_REFERER'])
        else:
            return HttpResponse(request.__dict__['environ']['HTTP_REFERER'])
    else:
        return HttpResponse("Enter Valid comments!")












        
def search(request):
    query = request.GET['query']
    if query != "":
        return render(request,"search.html",{"post_list": Post.objects.filter(title__icontains = query)})        
    else:
        return redirect("/")