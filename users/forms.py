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

    # def is_valid(self):
    #     return not BooksUser.objects.filter(username=self.cleaned_data.get('username')).exists()
    #     # and (self.clepassword1 == self.password2)

    # def save(self):
    #     user = BooksUser(username=self.cleaned_data.get('username'), password=self.cleaned_data.get('password'),
    #                      age=self.cleaned_data.get('age'))
    #     user.save()

    # username = forms.CharField(max_length=40, label="Username")
    # password1 = forms.CharField(max_length=150, label="Password")
    # password2 = forms.CharField(max_length=150, label="Password")
    # age = forms.IntegerField(label='Age', min_value=0)
    # REQUIRED_FIELDS = [username, password1, password2]
    #
