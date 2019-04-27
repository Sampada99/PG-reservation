from django import forms
 
from .models import Help_and_Support
 
 
class Help_and_SupportForm(forms.ModelForm):
    class Meta:
        model = Help_and_Support
        exclude = []