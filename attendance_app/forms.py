from django import forms
from attendance_app.models import *

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Images
        fields = ('document', )

class VideoForm(forms.ModelForm):
    class Meta:
        model = Upload_Video
        fields = ('upload_Video', )