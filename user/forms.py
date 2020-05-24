from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.forms import TextInput, EmailInput, FileInput, Select

from home.models import UserProfile


class SignUpFormForm(UserCreationForm):
    username = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=200)
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')


class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
        widgets = {
            'username'  : TextInput(attrs={'class': 'form-control', 'placeholder': 'Kullanıcı Adı'}),
            'email'     : EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'first_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'İsim'}),
            'last_name'  : TextInput(attrs={'class': 'form-control', 'placeholder': 'Soyisim'})
        }


CITY = [
    ('Istanbul', 'Istanbul'),
    ('Ankara', 'Ankara'),
    ('Izmir', 'Izmir'),
]


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('phone', 'address', 'city', 'country', 'image')
        widgets = {
            'phone'     : TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefon Numarası'}),
            'address'   : TextInput(attrs={'class': 'form-control', 'placeholder': 'Adres'}),
            'city'      : Select(attrs={'class': 'selectpicker', 'data-style': 'btn-white btn-lg', 'data-width': '100%',
                                        'data-live-search': 'True', 'placeholder': 'Şehir'}, choices=CITY),
            'country'   : TextInput(attrs={'class': 'form-control', 'placeholder': 'Ülke'}),
            'image'     : FileInput(attrs={'class': 'form-control', 'placeholder': 'Profil Resmi'})
        }
