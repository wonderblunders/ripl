# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-27 13:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('riplInd', '0016_callme_remarks'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='callme',
            name='remarks',
        ),
    ]
