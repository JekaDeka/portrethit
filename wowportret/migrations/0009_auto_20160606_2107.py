# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-06 18:07
from __future__ import unicode_literals

from django.db import migrations, models
import wowportret.models


class Migration(migrations.Migration):

    dependencies = [
        ('wowportret', '0008_auto_20160531_2359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='docfile',
            field=models.FileField(upload_to=wowportret.models.content_file_name, validators=[wowportret.models.Document.validate_image]),
        ),
    ]
