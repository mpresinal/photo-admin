# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-01 15:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photoadmin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photographer',
            name='water_mark_file',
            field=models.ImageField(blank=True, db_column='water_mark_file', null=True, upload_to=''),
        ),
    ]