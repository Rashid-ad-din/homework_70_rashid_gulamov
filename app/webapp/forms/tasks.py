from django import forms
from django.forms import Textarea, TextInput, Select, widgets, ModelMultipleChoiceField
from django.forms.widgets import ChoiceWidget, CheckboxSelectMultiple, SelectMultiple

from webapp.models import Task, Type, State


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
