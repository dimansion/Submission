# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-18 21:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0002_auto_20161118_2058'),
    ]

    operations = [
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('fk_form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='package.Submission')),
            ],
        ),
    ]
