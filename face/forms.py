from django.forms import ModelForm
from django import forms
from face.models import Photo

class PhotoForm(ModelForm):
    class Meta:
        model = Photo
