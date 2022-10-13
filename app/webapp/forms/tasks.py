from django import forms
from django.forms import Textarea, TextInput
from django.forms.widgets import SelectMultiple

from webapp.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('summary', 'description', 'state', 'type')
        widgets = {
            'summary': TextInput(attrs={
                'class': "form-control w-75",
            }),
            'description': Textarea(attrs={
                'class': "form-control w-75",
            }),
            'state': SelectMultiple(attrs={
                'class': "form-control w-75"
            }),
            'type': SelectMultiple(attrs={
                'class': "form-control w-75"
            })
        }


class SearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label='Найти', widget=TextInput(attrs={
        'class': 'mr-3',
        'style': 'width: 350px;'}
    ))
