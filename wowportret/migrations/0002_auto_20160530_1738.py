# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-30 14:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wowportret', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='docfile',
            field=models.FileField(upload_to='tmp_images/%Y/%m/%d'),
        ),
    ]