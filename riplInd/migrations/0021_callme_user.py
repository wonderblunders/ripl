# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-28 11:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('riplInd', '0020_remove_callme_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='callme',
            name='user',
            field=models.CharField(default=1, max_length=45),
            preserve_default=False,
        ),
    ]
