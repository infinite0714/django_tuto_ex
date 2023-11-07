from django import forms
from myapp.models import Dreamreal

class Loginform(forms.Form):
    user = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())

    def clean_user(self):
        username = self.cleaned_data.get("username")
        dbuser = Dreamreal.objects.filter(name = username)

        if not dbuser:
            raise forms.ValidationError("Username does not exist")
        return username