from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import TextInput, PasswordInput, EmailInput


class LoginForm(forms.Form):
    username = forms.CharField(required=True, label='Логин',
                               widget=forms.PasswordInput(attrs={'class': "form-control w-75"}))
    password = forms.CharField(required=True, label='Пароль',
                               widget=forms.PasswordInput(attrs={'class': "form-control w-75"}))
    next = forms.CharField(required=False, widget=forms.HiddenInput)


class CustomUserCreationForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', strip=False, required=True, widget=forms.PasswordInput)
    password_confirm = forms.CharField(label='Подтвердите пароль', strip=False, required=True,
                                       widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'password', 'password_confirm', 'first_name', 'last_name', 'email')
        widgets = {
            'username': TextInput(attrs={'class': "form-control w-75"}),
            'password': PasswordInput(attrs={'class': "form-control w-75"}),
            'password_confirm': PasswordInput(attrs={'class': "form-control w-75"}),
            'first_name': TextInput(attrs={'class': "form-control w-75"}),
            'last_name': TextInput(attrs={'class': "form-control w-75"}),
            'email': EmailInput(attrs={'class': "form-control w-75"}),

        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        if password and password_confirm and password != password_confirm:
            raise ValidationError('Пароли не совпадают')
        first_name = cleaned_data.get('first_name')
        if not first_name:
            raise ValidationError('Поле "Имя" обязательно к заполнению')
        email = cleaned_data.get('email')
        if not email:
            raise ValidationError('Поле "email" обязательно к заполнению')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('password'))
        # user.groups.add('user')
        if commit:
            user.save()
        return user
