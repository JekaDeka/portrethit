from django.db import models
from django.forms import ModelForm
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Document(models.Model):
    docfile = models.FileField(upload_to='tmp_img/')

    def __str__(self):
        return self.name
