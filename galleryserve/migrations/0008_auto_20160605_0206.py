# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-04 23:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('galleryserve', '0007_auto_20160605_0138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='galleryserve.Gallery'),
        ),
    ]
