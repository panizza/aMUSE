from basetyzer.models import Item, Scan, Photo, Comment, Action
from utils.helpers import save_image
from utils.helpers import send_email
from django.utils.http import int_to_base36
from django.contrib.auth.tokens import default_token_generator
from aMuse.settings import SITE_URL
from django.core.urlresolvers import reverse


def save_experience_data(experience, my_experience, user, user_created):
    """
    Save all the actions into the database. Return a json and a status code
    :rtype : application/json, int
    :param experience: JSON that contains all the actions
    :param my_experience: Experience's instance
    :param user: User's instance
    :param user_created: True/False. is CustomUser instance created now?
    """
    for exp in experience:
        action = Action()
        action.date_performed = exp['date']
        action.experience = my_experience
        if exp.get('type', '') == 'scan' and exp.get('id'):
            try:
                item = Item.objects.get(id=exp['id'])
            except Item.DoesNotExist:
                my_experience.delete()
                if user_created:
                    user.delete()
                return {
                           "status": "error",
                           "error": "Item does not exist"
                }, 404
            scan = Scan.objects.create(content=item)
            action.scan = scan
        if not exp.get('photo', '') == '':
            name, content = save_image(exp['photo'])
            photo = Photo()
            photo.content.save(name, content)
            action.photo = photo
        if not exp.get('text', '') == '':
            comment = Comment.objects.create(content=exp['text'])
            action.comment = comment
        action.save()
    return {
               "status": "saved",
               "error": ""
    }, 200


def generate_url_reset(user):
    """
    Generate a URL. The first part is a global setting, the second is
    created dinamically
    :param user: a standard User instance
    :return: string, the entire url
    """
    uid = int_to_base36(user.pk)
    token = default_token_generator.make_token(user)
    url = reverse('reset_password_new_user', args=[uid, token])
    return SITE_URL + url


def register_new_user(user):
    """
    Register a new User
        1. Flag the user as inactive
        2. Create the link for the password creation
        3. Send the email

    :param user: the User's instance
    """
    user.is_active = False
    user.set_unusable_password()
    user.save()

    url = generate_url_reset(user)
    #TODO: mettere un body decente per l'email
    send_email(user.email, url, 'aMUX Registration Confirm')
