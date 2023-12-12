from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label=u'Логин', widget=forms.TextInput(attrs={
      'class': 'form-control',
      'placeholder': 'Введите Логин'
    }))
    # user_email = forms.EmailField(widget=forms.EmailField)
    password = forms.CharField(label=u'Пароль', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите Пароль'
    }))

    class Meta:
        model = User
        fields = ['username', 'password']


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': "Введите ваш Логин"
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Создайте Пароль'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Повторите Пароль'
    }))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'password1', 'password2']
