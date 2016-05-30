from django.db import models
from django.forms import ModelForm


class Document(models.Model):
    docfile = models.FileField(upload_to='tmp_images/')
