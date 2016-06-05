# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-05 17:26
from __future__ import unicode_literals

from django.db import migrations
import galleryserve.thumbs


class Migration(migrations.Migration):

    dependencies = [
        ('galleryserve', '0012_auto_20160605_2024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='image',
            field=galleryserve.thumbs.ImageWithThumbsField(blank=True, upload_to='galleryserve/images'),
        ),
    ]
