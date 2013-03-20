from django.utils import six
from hashlib import sha1
from basetyzer.models import SuperQRCode


def create_qr(my_date, timestamp):
    edit_timestamp = my_date.replace(microsecond=0, tzinfo=None)
    value = sha1(six.text_type(edit_timestamp) + six.text_type(timestamp)) \
        .hexdigest()
    return "%s" % value