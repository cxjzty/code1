# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-11 09:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('one', '0003_marketgoods_markettype'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_username', models.CharField(max_length=16, unique=True)),
                ('u_password', models.CharField(max_length=32)),
                ('u_icon', models.ImageField(upload_to='static/uploadfiles/icons')),
                ('u_level', models.IntegerField(default=1)),
                ('u_email', models.CharField(max_length=64)),
                ('u_phone', models.CharField(max_length=32)),
                ('u_sex', models.NullBooleanField(default=True)),
            ],
        ),
    ]
