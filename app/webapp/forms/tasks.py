from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets, ModelChoiceField, Textarea, TextInput, CheckboxSelectMultiple

from webapp.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('summary', 'description', 'state', 'type')

        widgets = {
            'summary': TextInput(attrs={
                'class': "form-control",
            }),
            'description': Textarea(attrs={
                'class': "form-control",
            }),
            'state': CheckboxSelectMultiple(attrs={
                'class': "form-control",
            }),
            'type': CheckboxSelectMultiple(attrs={
                'class': "form-control",
            })
        }
