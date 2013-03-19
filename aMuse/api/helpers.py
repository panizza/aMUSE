from aMuse.basetyzer.models import Item, Scan, Photo, Comment, Action
from aMuse.utils.helpers import save_image


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