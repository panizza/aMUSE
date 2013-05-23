from django import forms
from basetyzer.models import Action, Photo, Comment


class UploadImageForm(forms.ModelForm):
    class Meta:
        model = Photo


class UploadCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
