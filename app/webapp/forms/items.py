from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets

from webapp.models import Item


class ItemForm(forms.Form):
    description = forms.CharField(
        max_length=250,
        required=True,
        label='Описание',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'style': 'max-width: 1000px;'
        })
    )
    description_details = forms.CharField(
        max_length=500,
        required=False,
        label='Подробное описание',
        widget=widgets.Textarea(attrs={
            'class': 'form-control',
            'style': 'max-width: 1000px;'
        })
    )
    state = forms.ChoiceField(
        choices=Item.CHOICES,
        required=True,
        label='Статус',
        widget=forms.Select(attrs={
            'class': 'form-control',
            'style': 'max-width: 150px;',
        })
    )
    date_to_do = forms.CharField(
        required=False,
        label='Дата',
        widget=widgets.TextInput(attrs={
            'class': 'form-control',
            'style': 'max-width: 400px;',
            'type': 'date',
        })
    )

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if len(description) < 2:
            raise ValidationError('Описание должно быть не менее 2-х символов')
        return description
