# Create your views here.
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.core.context_processors import csrf

import webinator.urls

def do_login(request):
    if request.POST:
        user_name= request.POST['email']
        pwd = request.POST['password']

        user = authenticate(username = user_name,password = pwd)

        if user is not  None:
            return render_to_response('webinator/user_details.html',{'user':user})
        else:
            url = reverse('login-fail',kwargs={'error':'login_fail'})
            return  HttpResponseRedirect(url)
            #return render_to_response('registration/login.html',{'state':'Wrong username or password'})

def show_login_error(request,error):
    if error == 'login_fail':
        return render_to_response('registration/login.html',{'state':'Wrong username or password'},
            context_instance =RequestContext(request))
    #This could be useful in future...maybe
    if error == 'logout':
        return render_to_response('registration/login.html',{'state':'You have been logout correctly'},
            context_instance =RequestContext(request))
