# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-24 12:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('riplInd', '0005_product_material'),
    ]

    operations = [
        migrations.AddField(
            model_name='dimension',
            name='desc',
            field=models.CharField(default=1, max_length=45),
            preserve_default=False,
        ),
    ]
