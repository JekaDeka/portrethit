from django.db import models
from django.forms import ModelForm
from django.utils.encoding import python_2_unicode_compatible


def content_file_name(instance, filename):
    return 'tmp_img/'.join(['mail_%Y%m%d', filename])


@python_2_unicode_compatible
class Document(models.Model):
    docfile = models.FileField(upload_to=content_file_name)

    def __str__(self):
        return self.name
