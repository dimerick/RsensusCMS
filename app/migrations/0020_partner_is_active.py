# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-29 19:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_auto_20190329_1413'),
    ]

    operations = [
        migrations.AddField(
            model_name='partner',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
