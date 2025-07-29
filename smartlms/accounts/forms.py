from django.contrib.auth.forms import UserCreationForm
from django import forms
from . import models


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    profile_picture = forms.ImageField(required=False)

    class Meta:
        model = models.User
        fields = ['username', 'email', 'password1', 'password2', 'role', 'profile_picture']