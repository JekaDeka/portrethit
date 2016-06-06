from django.db import models
from django.forms import ModelForm
from django.utils.crypto import get_random_string
from django.core.exceptions import ValidationError
import re


def content_file_name(instance, filename):
    ext = filename.split('.')
    filename = get_random_string(length=32) + "." + ext[1]
    return '/'.join(['tmp_img', filename])


class Document(models.Model):

    def validate_image(fieldfile_obj):
        filesize = fieldfile_obj.file.size
        megabyte_limit = 5.0
        if filesize > megabyte_limit * 1024 * 1024:
            raise ValidationError("Max file size is %sMB" %
                                  str(megabyte_limit))

    docfile = models.FileField(
        upload_to=content_file_name)
