from django.db import models
from django.core.exceptions import ValidationError
import PIL
from PIL import ImageOps
from ckeditor.fields import RichTextField
from galleryserve.thumbs import ImageWithThumbsField
from django.utils.encoding import python_2_unicode_compatible


class Gallery(models.Model):
    title = models.CharField(max_length=200, help_text="Title of gallery")
    image = ImageWithThumbsField(
        blank=True, upload_to='galleryserve/images', sizes=((125, 125), (415, 415)))
    content = RichTextField(
        blank=True, help_text="Mini description of gallery")
    height = models.IntegerField(blank=True, default=600,
                                 help_text="Height images should be resized to in pixels")
    width = models.IntegerField(blank=True, default=800,
                                help_text="Width images should be resized to in pixels")
    random = models.BooleanField(default=False,
                                 help_text="If selected, the sort numbers will be ignored and your "
                                 "gallery objects will be generated in random order.")
    resize = models.BooleanField(default=True,
                                 help_text="If selected, the dimensions specified above will be used"
                                 " to scale and crop the uploaded image")
    quality = models.IntegerField(u'Image Quality', default=85,
                                  help_text="An integer between 0-100. 100 will result in the largest "
                                  "file size.")

    parent = models.ForeignKey(
        'self', blank=True, null=True, related_name='children')

    has_child = models.BooleanField(default=False)

    is_baget = models.BooleanField(
        default=False, help_text="Is it baguette gallery")

    class Meta:
        ordering = ('title',)
        verbose_name_plural = 'galleries'

    def get_url(self):
        url = '/gallery/' + str(self.id) + '/'
        return url

    # def __unicode__(self):
    #     return u'%s' % (self.title)
    def __str__(self):
        p_list = self._recurse_for_parents(self)
        p_list.append(self.title)
        return self.get_separator().join(p_list)

    def __unicode__(self):
        p_list = self._recurse_for_parents(self)
        p_list.append(self.title)
        return self.get_separator().join(p_list)

    def _recurse_for_parents(self, cat_obj):
        p_list = []
        if cat_obj.parent_id:
            p = cat_obj.parent
            p_list.append(p.title)
            more = self._recurse_for_parents(p)
            p_list.extend(more)
        if cat_obj == self and p_list:
            p_list.reverse()
        return p_list

    def get_separator(self):
        return ' :: '

    def _parents_repr(self):
        p_list = self._recurse_for_parents(self)
        return self.get_separator().join(p_list)
    _parents_repr.short_description = 'Gallery parents'

    def save(self, **kwargs):
        p_list = self._recurse_for_parents(self)
        if self.title in p_list:
            raise ValidationError(
                'You must not save a category in itself')
        super(Gallery, self).save()
        if self.image:
            filename = self.image.path
            image = PIL.Image.open(filename)
            if self.resize:
                try:
                    width = self.width
                except:
                    width = 800
                try:
                    height = self.height
                except:
                    height = 600
                size = (width, height)
                image = ImageOps.fit(image, size, PIL.Image.ANTIALIAS)
            image.save(filename, quality=self.quality)

    # @models.permalink
    # def get_absolute_url(self):
    #     return ('category_index', (), {'category': self.slug})


#@python_2_unicode_compatible
class Item(models.Model):
    image = ImageWithThumbsField(
        blank=True, upload_to='galleryserve/images', sizes=((125, 125), (415, 415)))
    gallery = models.ForeignKey(Gallery, related_name='items')
    alt = models.CharField(max_length=100, blank=True,
                           help_text="This will be used for the image alt attribute")
    title = models.CharField(max_length=100, blank=True,
                             help_text="This will be used for the image or content title attribute")
    credit = models.CharField(max_length=200, blank=True,
                              help_text="Use this field to credit the image or content creator")
    video_url = models.URLField('video url', blank=True,
                                help_text="Enter the url of the video to be embedded")
    url = models.CharField('target url', blank=True, max_length=200,
                           help_text="URL to which the image will be linked.")
    content = models.TextField(blank=True, help_text="Use this field to "
                               "add html content associated with the item")
    sort = models.IntegerField(default=0,
                               help_text="Items will be displayed in their sort order")

    price = models.IntegerField(default=0, help_text="Price for item")

    class Meta:
        ordering = ('-title', )

    def __unicode__(self):
        return u'%s' % (self.alt)

    def save(self, **kwargs):
        super(Item, self).save()
        if self.image:
            filename = self.image.path
            image = PIL.Image.open(filename)
            if self.gallery.resize:
                try:
                    width = self.gallery.width
                except:
                    width = 800
                try:
                    height = self.gallery.height
                except:
                    height = 600
                size = (width, height)
                image = ImageOps.fit(image, size, PIL.Image.ANTIALIAS)
            image.save(filename, quality=85)
