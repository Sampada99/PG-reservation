from django import forms
 
from .models import  Custdetails

class CustdetailsForm(forms.ModelForm):
    Date_of_Birth = forms.DateField(help_text='Required. Format: YYYY-MM-DD')

    class Meta:

        model =  Custdetails
        exclude = []
 