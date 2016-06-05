# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-05 17:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galleryserve', '0011_auto_20160605_2024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='width',
            field=models.IntegerField(blank=True, default=800, help_text='Width images should be resized to in pixels'),
        ),
    ]
