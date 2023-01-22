from django import forms
from reviews.models import BooksUser


class UserForm(forms.ModelForm):
    pass

    class Meta:
        model = BooksUser
        widgets = {
           'password': forms.PasswordInput(),
        }
        fields = ('username', 'password', 'age')
