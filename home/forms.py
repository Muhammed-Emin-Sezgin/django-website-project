from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SearchForm(forms.Form):
    query = forms.CharField(label='search', max_length=100, required=False)
    category = forms.CharField(label='category', max_length=20, required=False)
    sehir = forms.CharField(label='sehir', max_length=20, required=False)


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=200)
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')
