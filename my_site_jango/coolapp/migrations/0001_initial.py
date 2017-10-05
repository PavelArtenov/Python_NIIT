# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-29 19:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('director', models.CharField(max_length=128)),
                ('actor', models.TextField()),
                ('about', models.TextField()),
                ('rating', models.IntegerField()),
                ('pub_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=64)),
                ('lastName', models.CharField(max_length=64)),
                ('patronymic', models.CharField(max_length=64)),
            ],
        ),
        migrations.AddField(
            model_name='film',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coolapp.Users'),
        ),
    ]
