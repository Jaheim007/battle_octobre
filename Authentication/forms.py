from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(max_length=128, widget=forms.PasswordInput) 
    
class SignInForm(UserCreationForm):
    email = forms.EmailField(max_length=150)
    
    class Meta:
        model = get_user_model()
        fields = (
            "first_name",
            "last_name", 
            "username", 
            "email",
            "password1",
            "password2",
        )