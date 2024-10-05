from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from django import forms

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ["username", "first_name", "last_name", "email", "bio", "avatar"]


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="username")
    password = forms.CharField(label="password", widget=forms.PasswordInput)
