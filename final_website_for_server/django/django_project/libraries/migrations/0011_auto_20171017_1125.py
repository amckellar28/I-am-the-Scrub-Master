# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-17 01:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraries', '0010_auto_20171016_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maps',
            name='height_field',
            field=models.IntegerField(default=0),
        ),
    ]