# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from basetyzer.models import Experience


@login_required()
def index(request):
    visit = Experience.objects.filter(user=request.user)

    return render(request, 'webinator/user_details.html', {
        'user': request.user,
        'message': '',
        'visit_confirmed': visit.filter(confirmed=True),
        'visit_not_confirmed': visit.exclude(confirmed=True)
    })
