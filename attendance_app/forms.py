from django import forms
from .models import  PhotoGallary

class ImageForm(forms.ModelForm):
    class Meta:
        model = PhotoGallary
        fields=['multipleimages']  
        label ={}
        widgets ={
            'multipleimages':forms.FileInput(attrs={'id':'myfile','class':'form-control-file','multiple':True}),
        } 