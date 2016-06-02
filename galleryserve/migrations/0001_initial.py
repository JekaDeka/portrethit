# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-02 10:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('height', models.IntegerField(blank=True, default=600, help_text='Height images should be resized to in pixels')),
                ('width', models.IntegerField(blank=True, default=800, help_text='Width images should be resized to in pixels')),
                ('random', models.BooleanField(default=False, help_text='If selected, the sort numbers will be ignored and your gallery objects will be generated in random order.')),
                ('resize', models.BooleanField(default=True, help_text='If selected, the dimensions specified above will be used to scale and crop the uploaded image')),
                ('quality', models.IntegerField(default=85, help_text='An integer between 0-100. 100 will result in the largest file size.', verbose_name='Image Quality')),
            ],
            options={
                'verbose_name_plural': 'galleries',
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='galleryserve/images')),
                ('alt', models.CharField(blank=True, help_text='This will be used for the image alt attribute', max_length=100)),
                ('title', models.CharField(blank=True, help_text='This will be used for the image or content title attribute', max_length=100)),
                ('credit', models.CharField(blank=True, help_text='Use this field to credit the image or content creator', max_length=200)),
                ('video_url', models.URLField(blank=True, help_text='Enter the url of the video to be embedded', verbose_name='video url')),
                ('url', models.CharField(blank=True, help_text='URL to which the image will be linked.', max_length=200, verbose_name='target url')),
                ('content', models.TextField(blank=True, help_text='Use this field to add html content associated with the item')),
                ('sort', models.IntegerField(default=0, help_text='Items will be displayed in their sort order')),
                ('gallery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='galleryserve.Gallery')),
            ],
            options={
                'ordering': ('sort',),
            },
        ),
    ]
