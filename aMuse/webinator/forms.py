from django import forms
from basetyzer.models import Action, Photo, Comment


class UploadImageForm(forms.Form):
    comment = forms.CharField(max_length=50)
    image = forms.ImageField()


    def save(self, exp):
        #photo = Photo.objects.create(content=)
        import pdb;pdb.set_trace()