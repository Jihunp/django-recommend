from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError

class CustomUserCreationForm(forms.Form):
    username = forms.CharField(label='Enter Username', min_length=5, max_length=120)
    email = forms.EmailField(label='Enter Email')
    password1 = forms.CharField(label='Enter password', widget=forms.PasswordInput)
    password2 =  forms.CharField(label= 'Confirm password', widget=forms.PasswordInput)

def clean_username(self):
    username = self.cleaned_data['username'].lower()
    u = User.objects.filter(username=username)
    if u.count():
        raise ValidationError("Username is already used")
    return username
