# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-21 04:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Personal', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='emailaddress',
        ),
    ]
