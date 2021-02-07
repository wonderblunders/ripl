# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-26 07:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('riplInd', '0006_dimension_desc'),
    ]

    operations = [
        migrations.CreateModel(
            name='spares',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_title', models.CharField(max_length=45)),
                ('s_image', models.ImageField(upload_to='media/upholstery', verbose_name='img')),
                ('v_title', models.CharField(max_length=45)),
                ('v_image', models.ImageField(upload_to='media/upholstery', verbose_name='img')),
            ],
        ),
    ]
