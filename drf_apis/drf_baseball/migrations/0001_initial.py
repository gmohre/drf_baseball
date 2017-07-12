# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-12 18:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NumpyDataStructure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('csv', models.FileField(upload_to='csvs/')),
                ('key', models.CharField(max_length=14)),
            ],
        ),
        migrations.CreateModel(
            name='NumpyFunction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('numpy_source', models.TextField(blank=True)),
                ('json', models.TextField(blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='numpydatastructure',
            name='numpy_function',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drf_baseball.NumpyFunction'),
        ),
    ]
