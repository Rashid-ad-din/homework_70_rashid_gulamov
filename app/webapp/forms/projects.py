from django import forms
from django.forms import Textarea, TextInput
from django.forms.widgets import DateInput

from webapp.models import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('title', 'description', 'date_start', 'date_end')
        widgets = {
            'title': TextInput(attrs={
                'class': "form-control w-75",
            }),
            'description': Textarea(attrs={
                'class': "form-control w-75",
            }),
            'date_start': TextInput(attrs={
                'class': "form-control w-75",
                'type': 'date',
                'value': '{{ project.date_start }}'
            }),
            'date_end': TextInput(attrs={
                'class': "form-control w-75",
                'type': 'date'
            })
        }
