from datetime import date as dt
from ajaxutils.decorators import ajax
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.forms.models import model_to_dict
from django.contrib.auth.decorators import login_required
from ajaxutils.http import json
from .helpers import save_experience_data
from basetyzer.models import Item, Experience, Exhibit, Tag, CustomUser, SuperQRCode
from api.helpers import register_new_user


@ajax(require="GET", login_required=False)
def get_exhibitions_list(request):
    """
    Return the public list of all the available exhibitions
    :rtype : application/json
    :param request: the standard request given by Django
    """
    today = dt.today()
    exhibitions = Exhibit.objects.available().values(
        'pk', 'name', 'description')

    return {
        'data': list(exhibitions)
    }, 200


@ajax(require="GET", login_required=False)
def get_exhibition_info(request, id_exhibition):
    """
    Return the information about one exhibitions
    :rtype : application/json
    :param request: the standard request given by Django
    :param id_exhibition: the pk of an exhibition instance
    """
    exhibition = get_object_or_404(Exhibit, pk=id_exhibition)
    return model_to_dict(exhibition, exclude=["owner"]), 200


@ajax(require="GET", login_required=False)
def get_items_list(request, id_exhibition):
    """
    Return the public list of all the available item assigned to a exhibit
    :rtype : application/json
    :param request: the standard request given by Django
    :param id_exhibition: the pk of an exhibition instance
    """
    exhibition = get_object_or_404(Exhibit, pk=id_exhibition)
    items = Item.objects.filter(exhibit=exhibition).values('pk', 'title')
    return {
        'data': list(items)
    }, 200


@ajax(require="GET", login_required=False)
def get_item_info(request, id_item):
    """
    Provides information regarding a specific object identified by id
    :rtype : application/json
    :param request: the standard request given by Django
    :param id_item: the pk of an item instance
    """
    item = get_object_or_404(Item, pk=id_item)
    item_json = model_to_dict(item, exclude=['exhibit', 'tag'])
    item_json['photo'] = item_json['photo'].url
    return item_json, 200


@ajax(require="POST", login_required=False)
@csrf_exempt
def save_experience(request):
    """
    Save all the experience information receiver by a POST request
    :rtype : application/json
    :param request: the standard request given by Django
    """
    data = json.loads(json.dumps(request.POST))
    if data.get('email') and data.get('confirm') and data.get('exp'):
        email = data['email']
        if data['confirm'] != SuperQRCode.objects.all()[0].text:
            return {
                        "status": "error",
                        "error": "qr code check failed",

            }, 400
        experience = data['exp']
        user, user_created = CustomUser.objects.get_or_create(username=email,
                                                        email=email)
        my_experience = Experience.objects.create(user=user)
        toret, status_code = save_experience_data(experience, my_experience,
                                                  user, user_created)
        if user_created:
            if status_code == 200:
                url = register_new_user(user, request)
                print url
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
@login_required
def api_test_for_some_code(request):
    pass
