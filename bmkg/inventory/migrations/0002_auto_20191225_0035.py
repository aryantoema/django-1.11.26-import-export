# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-12-25 00:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kelembaban',
            name='tanggal',
            field=models.DateField(blank=True, null=True, unique=True),
        ),
    ]
