# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-30 20:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galleryserve', '0016_auto_20160630_2348'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='has_child',
            field=models.BooleanField(default=False),
        ),
    ]
