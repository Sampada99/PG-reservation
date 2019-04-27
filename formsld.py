from django import forms
 
from .models import  Landdetails

class  LanddetailsForm(forms.ModelForm):
    class Meta:
        model =  Landdetails
        exclude = []
 