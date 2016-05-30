# -*- coding: utf-8 -*-
from django import forms
from django.core.validators import validate_email, RegexValidator


class ContactForm(forms.Form):
    contact_name = forms.CharField(
        label='Ваше имя', required=True, max_length=70)
    contact_phone = forms.CharField(
        label='Ваш телефон', required=True, max_length=20)
    contact_email = forms.EmailField(
        label='Ваша почта', required=True, max_length=70)
    content = forms.CharField(
        label='Ваше сообщение',
        required=False,
        widget=forms.Textarea
    )
    docfile = forms.FileField(label='Ваше фото',
                              widget=forms.FileInput, required=False)

    # the new bit we're adding
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['contact_name'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Иван'})
        self.fields['contact_phone'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': '+7 (987) 654-32-11'})
        self.fields['contact_email'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'ivan@mail.ru'})
        self.fields['content'].widget.attrs.update(
            {'class': 'form-control', 'rows': '3'})

        self.fields['docfile'].widget.attrs.update(
            {'class': 'form-control-file'})
