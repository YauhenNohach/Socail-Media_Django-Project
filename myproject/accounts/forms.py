from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from django import forms

from .models import CustomUser

# , Rating


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ["username", "first_name", "last_name", "email", "bio", "avatar"]


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="username")
    password = forms.CharField(label="password", widget=forms.PasswordInput)


# class RatingForm(forms.ModelForm):
#     class Meta:
#         model = Rating
#         fields = ["score"]
#         widgets = {
#             "score": forms.RadioSelect(choices=[(i, str(i)) for i in range(1, 11)]),
#         }
