from ajaxutils.decorators import ajax
from django.contrib.auth.models import User
from .helpers import save_experience_data
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.forms.models import model_to_dict
from basetyzer.models import Item, Experience
from ajaxutils.http import json


@ajax(require="GET", login_required=False)
def get_item(request, id_item):
    """ Provides information regarding a specific object identified by id
    """
    item = get_object_or_404(Item, pk=id_item)
    item_json = model_to_dict(item, exclude=['exhibit'])
    item_json['tag'] = model_to_dict(Tag.objects.get(pk=int(item_json['tag'])))
    item_json['photo'] = item_json['photo'].url
    return item_json


@ajax(require="POST", login_required=False)
@csrf_exempt
def visit_save(request):
    """ Save all the experience information receiver by a POST request
    :param request: the standard request given by Django
    """
    data = json.loads(json.dumps(request.POST))
    import pdb;pdb.set_trace()
    if data.get('email') and data.get('confirm') and data.get('exp'):
        email = data['email']
        #TODO[panizza]: y confirm isn't used?!
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