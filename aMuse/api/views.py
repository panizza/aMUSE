from ajaxutils.decorators import ajax
from django.contrib.auth.models import User
from .helpers import save_experience_data
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.forms.models import model_to_dict
from basetyzer.models import Item, Experience, Exhibit, Tag
from ajaxutils.http import json
from datetime import date as dt


@ajax(require="GET", login_required=False)
def get_exhibitions_list(request):
    """ Return the public list of all the available exhibitions
    :rtype : application/json
    :param request: the standard request given by Django
    """
    today = dt.today()
    exhibitions = Exhibit.objects\
        .exclude(date_end__lt=today)\
        .exclude(date_begin__gt=today)\
        .values('pk', 'name', 'description')
    return {
        'data': list(exhibitions)
    }, 200


@ajax(require="GET", login_required=False)
def get_exhibition_info(request, id_exhibition):
    """ Return the information about one exhibitions
    :rtype : application/json
    :param request: the standard request given by Django
    :param id_exhibition: the pk of an exhibition instance
    """
    exhibition = get_object_or_404(Exhibit, pk=id_exhibition)
    return model_to_dict(exhibition, exclude=["owner"]), 200


@ajax(require="GET", login_required=False)
def get_items_list(request, id_exhibition):
    """ Return the public list of all the available item assigned to a exhibit
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
    """ Provides information regarding a specific object identified by id
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
def visit_save(request):
    """ Save all the experience information receiver by a POST request
    :rtype : application/json
    :param request: the standard request given by Django
    """
    data = json.loads(json.dumps(request.POST))
    if data.get('email') and data.get('confirm') and data.get('exp'):
        email = data['email']
        #TODO[panizza]: why confirm isn't used?!
        confirm = data['confirm']
        experience = data['exp']
        user, user_created = User.objects.get_or_create(username=email,
                                                        email=email)
        my_experience = Experience.objects.create(user=user)
        toret, status_code = save_experience_data(experience, my_experience,
                                                  user, user_created)
        return toret, status_code
    else:
        return {
                   "status": "error",
                   "error": "JSON malformed"
        }, 400