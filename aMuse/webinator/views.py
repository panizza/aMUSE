# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


@login_required()
def index(request):
    if request.GET:
        return render(request, 'webinator/user_details.html', {
            'user': request.user, 'message': ''})
    else:
        logout(request)
        return render(request, 'registration/login.html', {
            'state': 'POST not allowed'}
        )
