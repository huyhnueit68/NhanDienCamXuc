from django import forms


class UploadFileForm(forms.Form):
    fullname = forms.CharField(max_length=50)
    classname = forms.CharField(max_length=50)
    file = forms.FileField()