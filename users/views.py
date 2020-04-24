from django.shortcuts import render,Http404,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate

# Create your views here.
def signup_handle(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        password = request.POST['password']
        confirm_password  = request.POST['password_confirm']
        if password == confirm_password:
            my_user = User.objects.create_user(username,password)
            my_user.first_name = fname
            my_user.last_name = lname
            my_user.save()
            return HttpResponse("Saved Successfully!")
        else:
            return HttpResponse("Passwords does not match!")
