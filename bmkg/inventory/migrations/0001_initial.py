# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-12-23 07:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Angin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tanggal', models.DateField(blank=True, unique=True)),
                ('jam0', models.CharField(blank=True, default=0, max_length=6)),
                ('jam1', models.CharField(blank=True, default=0, max_length=6)),
                ('jam2', models.CharField(blank=True, default=0, max_length=6)),
                ('jam3', models.CharField(blank=True, default=0, max_length=6)),
                ('jam4', models.CharField(blank=True, default=0, max_length=6)),
                ('jam5', models.CharField(blank=True, default=0, max_length=6)),
                ('jam6', models.CharField(blank=True, default=0, max_length=6)),
                ('jam7', models.CharField(blank=True, default=0, max_length=6)),
                ('jam8', models.CharField(blank=True, default=0, max_length=6)),
                ('jam9', models.CharField(blank=True, default=0, max_length=6)),
                ('jam10', models.CharField(blank=True, default=0, max_length=6)),
                ('jam11', models.CharField(blank=True, default=0, max_length=6)),
                ('jam12', models.CharField(blank=True, default=0, max_length=6)),
                ('jam13', models.CharField(blank=True, default=0, max_length=6)),
                ('jam14', models.CharField(blank=True, default=0, max_length=6)),
                ('jam15', models.CharField(blank=True, default=0, max_length=6)),
                ('jam16', models.CharField(blank=True, default=0, max_length=6)),
                ('jam17', models.CharField(blank=True, default=0, max_length=6)),
                ('jam18', models.CharField(blank=True, default=0, max_length=6)),
                ('jam19', models.CharField(blank=True, default=0, max_length=6)),
                ('jam20', models.CharField(blank=True, default=0, max_length=6)),
                ('jam21', models.CharField(blank=True, default=0, max_length=6)),
                ('jam22', models.CharField(blank=True, default=0, max_length=6)),
                ('jam23', models.CharField(blank=True, default=0, max_length=6)),
                ('publish', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Kelembaban',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tanggal', models.DateField(blank=True, unique=True)),
                ('jam0', models.IntegerField(default=0)),
                ('jam1', models.IntegerField(default=0)),
                ('jam2', models.IntegerField(default=0)),
                ('jam3', models.IntegerField(default=0)),
                ('jam4', models.IntegerField(default=0)),
                ('jam5', models.IntegerField(default=0)),
                ('jam6', models.IntegerField(default=0)),
                ('jam7', models.IntegerField(default=0)),
                ('jam8', models.IntegerField(default=0)),
                ('jam9', models.IntegerField(default=0)),
                ('jam10', models.IntegerField(default=0)),
                ('jam11', models.IntegerField(default=0)),
                ('jam12', models.IntegerField(default=0)),
                ('jam13', models.IntegerField(default=0)),
                ('jam14', models.IntegerField(default=0)),
                ('jam15', models.IntegerField(default=0)),
                ('jam16', models.IntegerField(default=0)),
                ('jam17', models.IntegerField(default=0)),
                ('jam18', models.IntegerField(default=0)),
                ('jam19', models.IntegerField(default=0)),
                ('jam20', models.IntegerField(default=0)),
                ('jam21', models.IntegerField(default=0)),
                ('jam22', models.IntegerField(default=0)),
                ('jam23', models.IntegerField(default=0)),
                ('publish', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Radiasi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tanggal', models.DateField(blank=True, unique=True)),
                ('R_06_07', models.CharField(blank=True, default=0, max_length=4)),
                ('R_07_08', models.CharField(blank=True, default=0, max_length=4)),
                ('R_08_09', models.CharField(blank=True, default=0, max_length=4)),
                ('R_09_10', models.CharField(blank=True, default=0, max_length=4)),
                ('R_10_11', models.CharField(blank=True, default=0, max_length=4)),
                ('R_11_12', models.CharField(blank=True, default=0, max_length=4)),
                ('R_12_13', models.CharField(blank=True, default=0, max_length=4)),
                ('R_13_14', models.CharField(blank=True, default=0, max_length=4)),
                ('R_14_15', models.CharField(blank=True, default=0, max_length=4)),
                ('R_15_16', models.CharField(blank=True, default=0, max_length=4)),
                ('R_16_17', models.CharField(blank=True, default=0, max_length=4)),
                ('R_17_18', models.CharField(blank=True, default=0, max_length=4)),
                ('R_18_19', models.CharField(blank=True, default=0, max_length=2)),
                ('R_19_20', models.CharField(blank=True, default=0, max_length=2)),
                ('R_20_21', models.CharField(blank=True, default=0, max_length=2)),
                ('R_21_22', models.CharField(blank=True, default=0, max_length=2)),
                ('R_22_23', models.CharField(blank=True, default=0, max_length=2)),
                ('R_23_00', models.CharField(blank=True, default=0, max_length=2)),
                ('R_00_01', models.CharField(blank=True, default=0, max_length=2)),
                ('R_01_02', models.CharField(blank=True, default=0, max_length=2)),
                ('R_02_03', models.CharField(blank=True, default=0, max_length=2)),
                ('R_03_04', models.CharField(blank=True, default=0, max_length=2)),
                ('R_04_05', models.CharField(blank=True, default=0, max_length=2)),
                ('R_05_06', models.CharField(blank=True, default=0, max_length=2)),
                ('publish', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Suhu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tanggal', models.DateField(blank=True, unique=True)),
                ('jam0', models.FloatField(default=0)),
                ('jam1', models.FloatField(default=0)),
                ('jam2', models.FloatField(default=0)),
                ('jam3', models.FloatField(default=0)),
                ('jam4', models.FloatField(default=0)),
                ('jam5', models.FloatField(default=0)),
                ('jam6', models.FloatField(default=0)),
                ('jam7', models.FloatField(default=0)),
                ('jam8', models.FloatField(default=0)),
                ('jam9', models.FloatField(default=0)),
                ('jam10', models.FloatField(default=0)),
                ('jam11', models.FloatField(default=0)),
                ('jam12', models.FloatField(default=0)),
                ('jam13', models.FloatField(default=0)),
                ('jam14', models.FloatField(default=0)),
                ('jam15', models.FloatField(default=0)),
                ('jam16', models.FloatField(default=0)),
                ('jam17', models.FloatField(default=0)),
                ('jam18', models.FloatField(default=0)),
                ('jam19', models.FloatField(default=0)),
                ('jam20', models.FloatField(default=0)),
                ('jam21', models.FloatField(default=0)),
                ('jam22', models.FloatField(default=0)),
                ('jam23', models.FloatField(default=0)),
                ('publish', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tekanan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tanggal', models.DateField(blank=True, unique=True)),
                ('jam0', models.FloatField(default=0)),
                ('jam1', models.FloatField(default=0)),
                ('jam2', models.FloatField(default=0)),
                ('jam3', models.FloatField(default=0)),
                ('jam4', models.FloatField(default=0)),
                ('jam5', models.FloatField(default=0)),
                ('jam6', models.FloatField(default=0)),
                ('jam7', models.FloatField(default=0)),
                ('jam8', models.FloatField(default=0)),
                ('jam9', models.FloatField(default=0)),
                ('jam10', models.FloatField(default=0)),
                ('jam11', models.FloatField(default=0)),
                ('jam12', models.FloatField(default=0)),
                ('jam13', models.FloatField(default=0)),
                ('jam14', models.FloatField(default=0)),
                ('jam15', models.FloatField(default=0)),
                ('jam16', models.FloatField(default=0)),
                ('jam17', models.FloatField(default=0)),
                ('jam18', models.FloatField(default=0)),
                ('jam19', models.FloatField(default=0)),
                ('jam20', models.FloatField(default=0)),
                ('jam21', models.FloatField(default=0)),
                ('jam22', models.FloatField(default=0)),
                ('jam23', models.FloatField(default=0)),
                ('publish', models.DateField(auto_now=True)),
            ],
        ),
    ]
