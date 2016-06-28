from django.db import models
from django.utils import timezone
from django.forms import ModelForm
from django.utils.crypto import get_random_string
from django.core.exceptions import ValidationError
from ckeditor.fields import RichTextField
import PIL
from PIL import ImageOps
from galleryserve.thumbs import ImageWithThumbsField
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


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = RichTextField()
    mini_text = RichTextField(blank=True, null=True, default="")
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)
    image = ImageWithThumbsField(
        blank=True, upload_to='galleryserve/images', sizes=((125, 125), (415, 415)))

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def save(self, **kwargs):
        super(Post, self).save()
        if self.image:
            filename = self.image.path
            image = PIL.Image.open(filename)
            image.save(filename, quality=80)
