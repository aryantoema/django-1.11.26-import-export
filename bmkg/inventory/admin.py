# -*- coding: utf-8 -*-
from __future__ import unicode_literals
#import decimal, csv

from django.contrib import admin
from django.http import HttpResponse
#from django.db.models import F

#from account.models import Akun, User
from import_export.admin import ImportExportModelAdmin
from .models import *
from .views import *

# Register your models here.

@admin.register(Kelembaban, Suhu, Tekanan, Angin)
class ViewAdmin(ImportExportModelAdmin):
    
    list_per_page = 31
    actions = (export_parameters, export_excels,)
    search_fields = ['tanggal']
    list_filter = ['tanggal']

@admin.register(Radiasi)
class ViewAdmin(ImportExportModelAdmin):
    actions = (export_parameters, export_xlsx,)
    list_per_page = 31
    search_fields = ['tanggal']
    list_filter = ['tanggal']


####################################################
