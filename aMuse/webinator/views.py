from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from basetyzer.models import Experience, CustomUser, SuperQRCode
from django.contrib.auth import login
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import base36_to_int
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from .helpers import create_qr
from datetime import datetime, timedelta, date
from django.shortcuts import get_object_or_404


def reset_password_new_user(request, uidb36, token):
    """
    Checks the link the user clicked and prompts for a new password
    :param request: the standard request given by Django
    :param uidb36: the id's hash
    :param token: token created dynamically
    """
    try:
        uid_int = base36_to_int(uidb36)
        user = CustomUser.objects.get(pk=uid_int)
    except (ValueError, OverflowError, CustomUser.DoesNotExist):
        user = None

    if user is not None and user.need_reset \
        and default_token_generator.check_token(user, token):
        validlink = True
        if request.method == "POST":
            form = SetPasswordForm(user, request.POST)
            if form.is_valid():
                form.save()
                user.need_reset = False
                user.save()
                user.backend = 'django.contrib.auth.backends.ModelBackend'
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
        else:
            form = SetPasswordForm(None)
    else:
        validlink = False
        form = None
    return render(request, 'registration/reset_password_complete.html', {
        'form': form,
        'validlink': validlink
    })


@login_required()
def index(request):
    """
    The main view. This view render a template with all the available
    experiences
    :param request: the standard request given by Django
    """
    visit = Experience.objects.filter(user=request.user)
    return render(request, 'webinator/user_details.html', {
        'user': request.user,
        'message': '',
        'visit_confirmed': visit.filter(confirmed=True),
        'visit_not_confirmed': visit.filter(confirmed=False)
    })


def qr_code_generator(request):
    """
    Generate the qr code (experiences validator) and put it into the db.
    :param request: the standard request given by Django
    """
    interval_sec = 60 #24 * 60 * 60 # 24h
    size = 500
    if SuperQRCode.objects.count() < 1:
        qr = create_qr(datetime.now(), (date.today() - date(2001, 1, 1)).days)
        qr_code = SuperQRCode.objects.create(text=qr)
    else:
        qr_code = SuperQRCode.objects.all()[0]
        if (qr_code.last_edit + timedelta(0, interval_sec)) < datetime.now():
            qr = create_qr(qr_code.last_edit,
                           (date.today() - date(2001, 1, 1)).days)
            qr_code.text = qr
            qr_code.save()
    return render(request, 'webinator/qr_code.html', {
        'size': size,
        'text': qr_code.text
    })

def action_list(request, experience_id):
    exp = get_object_or_404(Experience,pk = experience_id)
    action = exp.action_set.all()
    return render(request,'webinator/imagelist.html',{'list':action})

def experience_preview(request):
    return render(request, 'webinator/preview.html')


