# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-21 06:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraries', '0018_auto_20171020_1354'),
    ]

    operations = [
        migrations.AddField(
            model_name='colleges',
            name='rank',
            field=models.CharField(default='3', max_length=140),
            preserve_default=False,
        ),
    ]
