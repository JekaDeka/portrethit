# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-04 15:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('galleryserve', '0003_auto_20160603_0014'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='child', to='galleryserve.Gallery'),
        ),
    ]
