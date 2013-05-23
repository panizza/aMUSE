from django.core.files.base import ContentFile
from StringIO import StringIO
from PIL import Image
from django.core.mail import BadHeaderError, send_mail
import hashlib
import base64
import re


def save_image(image_b64):
    """
    Return image name and the real image from a base64
    :param image_b64: base64 encoded string
    """
    image = base64.decodestring(image_b64.replace(' ', '+'))
    image_sha1 = hashlib.sha1(image).hexdigest()
    extension = '.' + Image.open(StringIO(image)).format.lower()
    return image_sha1 + extension, ContentFile(image)

from django_rq.decorators import job
@job('default')
def send_email(email, body, subject):
    if email_validator(email):
        try:
            send_mail(subject, body, "no-reply@amux.net", [email],
                      fail_silently=True)
        except BadHeaderError:
            return 'failed'
    return 'success'


def email_validator(email):
    """
    An email validator
    """
    if re.match('([\w\-\.\+]+@(\w[\w\-]+\.)+[\w\-]+)', email):
        return True
    return False
