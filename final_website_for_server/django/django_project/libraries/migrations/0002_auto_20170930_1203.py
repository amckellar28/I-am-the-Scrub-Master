# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-30 02:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraries', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='library',
            name='number',
            field=models.CharField(max_length=140),
        ),
    ]
