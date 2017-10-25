# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-20 00:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraries', '0013_auto_20171020_1045'),
    ]

    operations = [
        migrations.AddField(
            model_name='colleges',
            name='description',
            field=models.TextField(default='wow'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='colleges',
            name='height_field',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='colleges',
            name='home_page',
            field=models.URLField(default='wow'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='colleges',
            name='image',
            field=models.ImageField(blank=True, height_field='height_field', null=True, upload_to='', width_field='width_field'),
        ),
        migrations.AddField(
            model_name='colleges',
            name='width_field',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='hotels',
            name='description',
            field=models.TextField(default='wow'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hotels',
            name='height_field',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='hotels',
            name='home_page',
            field=models.URLField(default='wow'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hotels',
            name='image',
            field=models.ImageField(blank=True, height_field='height_field', null=True, upload_to='', width_field='width_field'),
        ),
        migrations.AddField(
            model_name='hotels',
            name='width_field',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='industries',
            name='description',
            field=models.TextField(default='wow'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='industries',
            name='height_field',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='industries',
            name='home_page',
            field=models.URLField(default='wow'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='industries',
            name='image',
            field=models.ImageField(blank=True, height_field='height_field', null=True, upload_to='', width_field='width_field'),
        ),
        migrations.AddField(
            model_name='industries',
            name='width_field',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='library',
            name='description',
            field=models.TextField(default='wow'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='library',
            name='height_field',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='library',
            name='home_page',
            field=models.URLField(default='wow'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='library',
            name='image',
            field=models.ImageField(blank=True, height_field='height_field', null=True, upload_to='', width_field='width_field'),
        ),
        migrations.AddField(
            model_name='library',
            name='width_field',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='malls',
            name='description',
            field=models.TextField(default='wow'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='malls',
            name='height_field',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='malls',
            name='home_page',
            field=models.URLField(default='wow'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='malls',
            name='image',
            field=models.ImageField(blank=True, height_field='height_field', null=True, upload_to='', width_field='width_field'),
        ),
        migrations.AddField(
            model_name='malls',
            name='width_field',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='museums',
            name='description',
            field=models.TextField(default='wow'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='museums',
            name='height_field',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='museums',
            name='home_page',
            field=models.URLField(default='wow'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='museums',
            name='image',
            field=models.ImageField(blank=True, height_field='height_field', null=True, upload_to='', width_field='width_field'),
        ),
        migrations.AddField(
            model_name='museums',
            name='width_field',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='parks',
            name='description',
            field=models.TextField(default='wow'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='parks',
            name='height_field',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='parks',
            name='home_page',
            field=models.URLField(default='wow'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='parks',
            name='image',
            field=models.ImageField(blank=True, height_field='height_field', null=True, upload_to='', width_field='width_field'),
        ),
        migrations.AddField(
            model_name='parks',
            name='width_field',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='restaurants',
            name='description',
            field=models.TextField(default='wow'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='restaurants',
            name='height_field',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='restaurants',
            name='home_page',
            field=models.URLField(default='wow'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='restaurants',
            name='image',
            field=models.ImageField(blank=True, height_field='height_field', null=True, upload_to='', width_field='width_field'),
        ),
        migrations.AddField(
            model_name='restaurants',
            name='width_field',
            field=models.IntegerField(default=0),
        ),
    ]