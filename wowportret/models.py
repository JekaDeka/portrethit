from django.db import models
from django.utils import timezone
from django.forms import ModelForm
from django.utils.crypto import get_random_string
from django.core.exceptions import ValidationError
from django.utils.html import strip_tags
from django.contrib import admin
from django.conf import settings
from ckeditor.fields import RichTextField
from PIL import ImageOps
from galleryserve.thumbs import ImageWithThumbsField
import re
import vk
import PIL


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

    def vk_wall_post(self):
        session = vk.Session(access_token=settings.VK_ACCESS_TOKEN)
        api = vk.API(session)
        api.wall.post(owner_id=settings.VK_GROUP_ID,
                      from_group=0, message=strip_tags(self.text))
        # print(strip_tags(self.text))

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

        self.vk_wall_post()
