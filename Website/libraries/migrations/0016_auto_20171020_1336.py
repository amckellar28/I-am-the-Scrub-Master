# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-20 03:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraries', '0015_auto_20171020_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colleges',
            name='image',
            field=models.ImageField(blank=True, height_field='height_field', null=True, upload_to='', width_field='width_field'),
        ),
    ]