# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-03 11:53
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coolapp', '0003_weather'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='email',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='film',
            name='rating',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)]),
        ),
    ]