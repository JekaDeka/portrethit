# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-11 19:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('galleryserve', '0022_auto_20160711_2227'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ('sort', '-id')},
        ),
    ]