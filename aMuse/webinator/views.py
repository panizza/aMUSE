# Create your views here.
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login
import webinator.urls

def do_login(request):
    if request.POST:
        user_name= request.POST['email']
        pwd = request.POST['password']

        user = authenticate(username = user_name,password = pwd)

        if user is not  None:
            return render_to_response('webinator/user_details.html',{'user':user})
        else:
            return render_to_response('registration/login.html',{'state':'Wrong username or password'})

