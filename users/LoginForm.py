from django import forms
from django.contrib.auth.forms import AuthenticationForm

from reviews.models import BooksUser
from users.forms import UserForm


class LoginForm(AuthenticationForm):
    pass
    class Meta:
        model = BooksUser
        widgets = {
            'password': forms.PasswordInput(),
        }
        fields = ('username', 'password')
