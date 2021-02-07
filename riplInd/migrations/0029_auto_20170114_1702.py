# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-14 11:32
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('riplInd', '0028_auto_20170114_1205'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='city',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='con_pref',
        ),
        migrations.AlterField(
            model_name='mblog',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 14, 17, 2, 1, 334000)),
        ),
        migrations.AlterField(
            model_name='product',
            name='cover',
            field=models.ImageField(upload_to='cover', verbose_name='cover image'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='prothumb', verbose_name='Thumbnail'),
        ),
    ]
