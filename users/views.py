from django.shortcuts import render,Http404,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.views.generic import TemplateView
from django.db import IntegrityError
from django.contrib.auth.models import Permission

class signUpView(TemplateView):
    template_name = "index.html"
    def post(self,request):
        try:
            fname = request.POST['fname']
            lname = request.POST['lname']
            email = request.POST['email']
            username = request.POST['username']
            password = request.POST['password']
            confirm_password  = request.POST['password_confirm']
            if password == confirm_password:
                my_user = User.objects.create_user(username,email,password)
                my_user.first_name = fname
                my_user.last_name = lname
                my_user.is_superuser = False
                my_user.is_staff = False
                #permission = Permission.objects.get(name= "posts post Can View post")
                my_user.save()
                return redirect("/")
            else:
                return HttpResponse("Passwords does not match!")
        except IntegrityError:
            return HttpResponse("Account Already exists!")        
        except Exception as ex:
            return HttpResponse(ex)
class loginView(TemplateView):
    template_name = "index.html"
    def post(self,request):
        try:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username = username,password = password)
            if user is not None:
                login(request,user)
                return redirect("/")
            else:
                return HttpResponse("Invalid Credentials!")    
        except Exception as ex:
            return HttpResponse(ex)    