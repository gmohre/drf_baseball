# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-11 20:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NumpyFunction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('numpy_source', models.TextField()),
                ('json', models.TextField()),
            ],
        ),
    ]
