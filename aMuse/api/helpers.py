import hashlib
import base64
from django.core.files.base import ContentFile
from StringIO import StringIO
from PIL import Image

def save_image(image_b64):
    """ return image name and the real image from a base64
    """
    image = base64.decodestring(image_b64.replace(' ', '+'))
    image_sha1 = hashlib.sha1(image).hexdigest()
    extension = '.' + Image.open(StringIO(image)).format.lower()
    return image_sha1 + extension, ContentFile(image)
