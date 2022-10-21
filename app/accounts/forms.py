from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(required=True, label='Логин',
                               widget=forms.PasswordInput(attrs={'class': "form-control w-75"}))
    password = forms.CharField(required=True, label='Пароль',
                               widget=forms.PasswordInput(attrs={'class': "form-control w-75"}))
    next = forms.CharField(required=False, widget=forms.HiddenInput)
