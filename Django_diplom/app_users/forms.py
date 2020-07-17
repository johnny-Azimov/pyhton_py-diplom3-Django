from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Электронная почта')
    first_name = forms.CharField(max_length=30, help_text='Имя')
    last_name = forms.CharField(max_length=150, help_text='Фамилия')


class Meta:
    model = User
    fields = ('username', 'email', 'password1', 'password2', 'first_name', 'last_name',)
