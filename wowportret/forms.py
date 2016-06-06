# -*- coding: utf-8 -*-
from django import forms
from django.core.validators import validate_email, RegexValidator
from django.template.defaultfilters import filesizeformat
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


class RestrictedFileField(forms.FileField):

    def __init__(self, *args, **kwargs):
        self.content_types = kwargs.pop('content_types', None)
        self.max_upload_size = kwargs.pop('max_upload_size', None)
        if not self.max_upload_size:
            self.max_upload_size = settings.MAX_UPLOAD_SIZE
        super(RestrictedFileField, self).__init__(*args, **kwargs)

    def clean(self, *args, **kwargs):
        data = super(RestrictedFileField, self).clean(*args, **kwargs)
        try:
            if data.content_type in self.content_types:
                if data.size > self.max_upload_size:
                    raise forms.ValidationError(_('File size must be under %s. Current file size is %s.') % (
                        filesizeformat(self.max_upload_size), filesizeformat(data.size)))
            else:
                raise forms.ValidationError(
                    _('File type (%s) is not supported.') % data.content_type)
        except AttributeError:
            pass

        return data


class RestrictedImageField(forms.ImageField):

    def __init__(self, *args, **kwargs):
        self.max_upload_size = kwargs.pop('max_upload_size', None)
        if not self.max_upload_size:
            self.max_upload_size = settings.MAX_UPLOAD_SIZE
        super(RestrictedImageField, self).__init__(*args, **kwargs)

    def clean(self, *args, **kwargs):
        data = super(RestrictedImageField, self).clean(*args, **kwargs)
        try:
            if data.size > self.max_upload_size:
                raise forms.ValidationError(_('File size must be under %s. Current file size is %s.') % (
                    filesizeformat(self.max_upload_size), filesizeformat(data.size)))
        except AttributeError:
            pass

        return data


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

    docfile = RestrictedImageField()
    # docfile = forms.FileField(label='Ваше фото',
    #                           widget=forms.FileInput, required=False)

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


class ItemForm(ContactForm):
    contact_item = forms.CharField(
        label='Ваш заказ', required=True, widget=forms.Textarea)
