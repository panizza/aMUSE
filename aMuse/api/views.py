from ajaxutils.decorators import ajax
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.forms.models import model_to_dict
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from ajaxutils.http import json
from .helpers import save_experience_data
from basetyzer.models import Item, Experience, Exhibit, SuperQRCode
from api.helpers import register_new_user
from sorl.thumbnail import get_thumbnail


@ajax(require="GET", login_required=False)
def get_item_info(request, hash_item):
    """
    Provides information regarding a specific object identified by id
    :rtype : application/json
    :param request: the standard request given by Django
    :param id_item: the pk of an item instance
    """
    item = get_object_or_404(Item, tag=hash_item)
    item_json = model_to_dict(item, exclude=['exhibit', 'tag'])
    try:
        thumbnail = get_thumbnail(item.photo, '200x200', format="PNG")
    except:
        thumbnail = item.photo
    else:
        item_json['photo'] = thumbnail.url
    return item_json, 200


@ajax(require="POST", login_required=False)
@csrf_exempt
def save_experience(request):
    """
    Save all the experience information receiver by a POST request
    :rtype : application/json
    :param request: the standard request given by Django
    """
    data = json.loads(request.body)
    if request.META['CONTENT_TYPE'] == "application/json" and data.get('email') and data.get('confirm') and data.get('exp'):
        email = data['email']
        if data['confirm'] != SuperQRCode.objects.all()[0].text:
            return {
                        "status": "error",
                        "error": "qr code check failed",

            }, 400
        experience = data['exp']
        user, user_created = User.objects.get_or_create(username=email,
                                                        email=email)
        my_experience = Experience.objects.create(user=user)
        toret, status_code = save_experience_data(experience, my_experience,
                                                  user, user_created)
        if user_created:
            if status_code == 200:
                url = register_new_user(user, request)
            else:
                user.delete()
        return toret, status_code
    else:
        return {
                   "status": "error",
                   "error": "JSON malformed"
        }, 400


######################################
##### ONLY FOR DEBUG! DO NOT EDIT#####
######################################
from django.http import HttpResponse
from utils.helpers import send_email
def api_test_for_some_code(request):
    job=send_email.delay('panizza01@gmail.com', 'exterminate', 'dalek')
    return HttpResponse("<a href='/django-rq/'>rq statistics</a>")
