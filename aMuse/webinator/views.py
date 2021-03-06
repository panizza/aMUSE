from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from basetyzer.models import Experience, SuperQRCode, Action, Item, Comment
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import base36_to_int
from django.http import HttpResponseRedirect, HttpResponse, Http404, HttpResponseForbidden
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from .helpers import create_qr
from datetime import datetime, timedelta, date
from django.shortcuts import get_object_or_404
from ajaxutils.decorators import ajax
from forms import UploadImageForm, UploadCommentForm


def reset_password_new_user(request, uidb36, token):
    """
    Checks the link the user clicked and prompts for a new password
    :param request: the standard request given by Django
    :param uidb36: the id's hash
    :param token: token created dynamically
    """
    try:
        uid_int = base36_to_int(uidb36)
        user = User.objects.get(pk=uid_int)
    except (ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and not user.has_usable_password() \
        and default_token_generator.check_token(user, token):
        validlink = True
        if request.method == "POST":
            form = SetPasswordForm(user, request.POST)
            if form.is_valid():
                user = form.save()
                user.is_active = True
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

    visit = Experience.objects.filter(user=request.user)
    return render(request, 'webinator/user_details.html', {
        'user': request.user,
        'message': '',
        'visit_public': visit.filter(public=True),
        'visit_not_public': visit.filter(public=False)
    })


def qr_code_generator(request):
    """
    Generate the qr code (experiences validator) and put it into the db.
    :param request: the standard request given by Django
    """
    interval_sec = 24 * 60 * 60 # 24h
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


@login_required
def action_list(request, experience_id):
    """
    (no docs)
    :param request: the standard request given by Django
    :param experience_id: the experience instance
    """
    exp = get_object_or_404(Experience, pk=experience_id)
    action = exp.action_set.all()
    return render(request, 'webinator/actionlist.html', {
        'lista': action,
        'exp_id': experience_id,
        'public': exp.public,
    })


def story_preview(request, uidb36, token):
    """
    (no docs)
    :param request: the standard request given by Django
    """
    uid_int = base36_to_int(uidb36)
    user = get_object_or_404(User, pk=uid_int)
    exp = user.experience_set.get(hash_url="{0}-{1}".format(uidb36, token))
    #TODO[lotto]: controllare if, non funziona
    if exp and ((request.user.is_authenticated() and exp.user == request.user) or (exp.public)):
        return render(request, 'webinator/photobook.html', {
            'action_list': exp.action_set.all(),
            'site_url': settings.SITE_URL,
        })
    else:
        return HttpResponseForbidden()


@csrf_exempt
@ajax(require='POST', login_required=True)
def edit_action(request, action_id):
    """
    Allow the user edit an action (only comments can be edited)
    :param request: the standard request given by Django
    :param action_id: the action instance
    """
    action = get_object_or_404(Action, pk=action_id)
    text_comment = request.POST.get('comment', None)
    #import pdb;pdb.set_trace()
    if not text_comment:
        return {
            "status": "error",
            "error": "Comment parameter not found"
        }, 404
    if action.comment:
        action.comment.content = text_comment
    else:
        action.comment = Comment()
    try:
        action.comment.save()
    except:
        return {
            "status": "error",
            "error": "Error while saving the comment"
        }, 500
    else:
        return {
            "status": "updated",
            "error": ""
        }, 200


@csrf_exempt
@ajax(require='GET', login_required=True)
def delete_action(request, action_id):
    """
    Allow the user to delete an action
    :param request: the standard request given by Django
    :param action_id: the action instance
    :return:
    """
    action = get_object_or_404(Action, pk=action_id)
    try:
        action.delete()
    except:
        return {
                   "status": "error",
                   "error": "Error while deleting the action"
        }, 404
    else:
        return {
                   "status": "deleted",
                   "error": ""
        }, 200


@csrf_exempt
@ajax(require='GET', login_required=True)
def delete_experience(request, experience_id):
    """
    Allow the user to delete an action
    :param request: the standard request given by Django
    :param experience_id: the experience instance
    :return:
    """
    experience = get_object_or_404(Experience, pk=experience_id)
    try:
        experience.delete()
    except:
        return {
                   "status": "error",
                   "error": "Error while deleting the experience"
        }, 404
    else:
        return {
                   "status": "deleted",
                   "error": ""
        }, 200


def view_error(request, error_id):
    if error_id == "0":
        return render(request, 'webinator/error.html', {'error': 'There was an error while loading data','id':error_id})
    elif error_id == "1":
        return render(request, 'webinator/error.html', {'error': 'There was an error while deleting this experience','id':error_id})
    elif error_id == "2":
        return render(request, 'webinator/error.html', {'error': 'There was an error while uploading the file!','id':error_id})

    raise Http404


def action_info(request, action_id):
    """
    Gets the information about an action
    :param request: the standard request
    :param action_id: id of the action to retrieve
    :return:
    """

    action = get_object_or_404(Action, pk=action_id)
    return render(request, 'webinator/action_edit.html', {
        'item': action,
    })
def scan_info(request,scan_id):
    """
    Gets the information about the scanned item
    :param request: standard request
    :param scan_id: scan id
    :return:
    """
    scan = get_object_or_404(Item, pk=scan_id)
    return render(request,'webinator/item_info.html',{'item' : scan,})

@login_required
def add_new_action(request, experience_id):
    """
    Handle the file upload for a new action
    :param request:
    :param exp_id: The experience id linked to the action
    :return:
    """
    user = get_object_or_404(User, id=request.user.id)
    exp = get_object_or_404(Experience, id=experience_id)
    action = Action(experience=exp, date_performed=datetime.now().strftime("%Y-%m-%d %H:%M"))
    if request.method == "POST":
        image_form = UploadImageForm(request.POST, request.FILES)
        comment_form = UploadCommentForm(request.POST)
        if not image_form.is_valid() and not comment_form.is_valid():
            return render(request, 'webinator/error.html', {'error_id': "2"})
        if image_form.is_valid():
            image = image_form.save()
            action.photo = image
        if comment_form.is_valid():
            comment = comment_form.save()
            action.comment = comment

        action.save()
        #return HttpResponseRedirect(reverse('action_list', args=[experience_id]))
        return HttpResponseRedirect(reverse('index'))

    else:
        return render(request, 'webinator/new_action.html', {
            'image_form': UploadImageForm(),
            'comment_form': UploadCommentForm()
        }
        )

@ajax(require='GET', login_required=True)
def publish_experience(request, experience_id):
    exp = get_object_or_404(Experience, pk=experience_id)
    exp.public = True
    exp.save()
    return HttpResponseRedirect(reverse('index'))


@login_required
def preview_experience(request, experience_id):
    exp = get_object_or_404(Experience, pk=experience_id)
    return render(request, 'webinator/preview_link.html', {'exp': exp, 'site_url': settings.SITE_URL})


@login_required
def confirm_publish(request,experience_id):
    return render(request,'webinator/confirm_message.html', {'exp_id': experience_id})


@login_required
def show_preview(request, experience_id):
    exp = get_object_or_404(Experience, pk=experience_id)
    return render(request, 'webinator/photobook.html', {
            'action_list': exp.action_set.all(),
            'site_url': settings.SITE_URL,
        })