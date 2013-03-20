from basetyzer.models import Item, Scan, Photo, Comment, Action
from utils.helpers import save_image, generate_url_reset
from utils.helpers import send_email


def save_experience_data(experience, my_experience, user, user_created):
    """ Save all the actions into the database. Return a json and a status code
    :rtype : application/json, status_code
    :param experience: JSON that contains all the actions
    :param my_experience: Experience's instance
    :param user: User's instance
    :param user_created: True/False. is User instance created now?
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


def register_new_user(user, request):
    """ Register a new user
        1. Flag the user as inactive
        2. Create the link for the password creation
        3. Send the email

    :param user: the user's instance
    """
    # 1. Flag the user as inactive and need_reset = True
    user.is_active = False
    user.save(commit=False)
    user.need_reset = True
    user.save()
    # 2. Create the link for the password creation
    url = generate_url_reset(user)
    print url
    return True
