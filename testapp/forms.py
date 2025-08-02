from django import forms 
from testapp.models import Ads,Contact

class ContactForm(forms.ModelForm):
    message = forms.CharField(max_length=250, required=True, widget=forms.Textarea(attrs={'rows':4,'placeholder':'Please Enter Message'}))
    mobile = forms.CharField(max_length=11,required=True,widget=forms.TextInput(attrs={'maxlength':10}))
    class Meta:
        model=Contact
        fields='__all__'