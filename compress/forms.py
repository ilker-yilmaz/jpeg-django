from django.forms import forms


class UploadForm(forms.Form):
    image = forms.FileField()