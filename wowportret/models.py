from django.db import models
from django.forms import ModelForm
from django.utils.crypto import get_random_string
import re


def content_file_name(instance, filename):
    ext = filename.split('.')
    filename = get_random_string(length=32) + "." + ext[1]
    return '/'.join(['tmp_img', filename])


class Document(models.Model):
    docfile = models.FileField(upload_to=content_file_name)
