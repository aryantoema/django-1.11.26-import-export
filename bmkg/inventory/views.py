# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#from django.shortcuts import render
import csv, decimal
#from datetime import datetime
#from datetime import timedelta
#from openpyxl import Workbook
#from openpyxl.styles import Font, Alignment, Border, Side, PatternFill
#from openpyxl.utils import get_column_letter

from datetime import datetime, date
#from bmkg.inventory.models import MyModel
import xlwt

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse

#from django.urls import reverse
from .models import *
from .forms import *

#FUNGSI DISPLAY
def index(request):
    return render(request, 'inv/index.html')

def view_kelembaban(request):
	datas = Kelembaban.objects.all()
	context = {
		'datas' : datas,
		'header' : 'Kelembaban',
	}
	return render(request, 'inv/kelembaban.html', context)

def view_suhu(request):
	datas = Suhu.objects.all()
	context = {
		'datas' : datas,
		'header' : 'Suhu',
	}
	return render(request, 'inv/suhu.html', context)

def view_tekanan(request):
	datas = Tekanan.objects.all()
	context = {
		'datas' : datas,
		'header' : 'Tekanan',
	}
	return render(request, 'inv/tekanan.html', context)

def view_angin(request):
	datas = Angin.objects.all()
	context = {
		'datas' : datas,
		'header' : 'Angin',
	}
	return render(request, 'inv/angin.html', context)

def view_radiasi(request):
	datas = Radiasi.objects.all()
	context = {
		'datas' : datas,
		'header' : 'Radiasi',
	}
	return render(request, 'inv/radiasi.html', context)



#FUNGSI TAMBAH_DATA
def add_data(request, cls):
	if request.method == "POST":
		form = cls(request.POST)
		if form.is_valid():
			form.save()
			return redirect('index')

	else:
		form = cls()
		return render(request, 'inv/add_new.html', {'form': form})

def add_kelembaban(request):
	return add_data(request, KelembabanForm)

def add_suhu(request):
	return add_data(request, SuhuForm)

def add_tekanan(request):
	return add_data(request, TekananForm)

def add_angin(request):
	return add_data(request, AnginForm)

def add_radiasi(request):
	return add_data(request, RadiasiForm)

#FUNGSI EDIT_DATA
def edit_data(request, pk, model, cls):
    data = get_object_or_404(model, pk=pk)

    if request.method == "POST":
        form = cls(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = cls(instance=data)

        return render(request, 'inv/edit_data.html', {'form': form})

def edit_kelembaban(request, pk):
    return edit_data(request, pk, Kelembaban, KelembabanForm)

def edit_suhu(request, pk):
    return edit_data(request, pk, Suhu, SuhuForm)

def edit_tekanan(request, pk):
    return edit_data(request, pk, Tekanan, TekananForm)

def edit_angin(request, pk):
    return edit_data(request, pk, Angin, AnginForm)

def edit_radiasi(request, pk):
    return edit_data(request, pk, Radiasi, RadiasiForm)

#FUNGSI DELETE
def delete_kelembaban(request, pk):

    template = 'inv/kelembaban.html'
    Kelembaban.objects.filter(id=pk).delete()

    datas = Kelembaban.objects.all()

    context = {
        'datas': datas,
    }

    return render(request, template, context)

def delete_suhu(request, pk):

    template = 'inv/suhu.html'
    Suhu.objects.filter(id=pk).delete()

    datas = Suhu.objects.all()

    context = {
        'datas': datas,
    }

    return render(request, template, context)

def delete_tekanan(request, pk):

    template = 'inv/tekanan.html'
    Tekanan.objects.filter(id=pk).delete()

    datas = Tekanan.objects.all()

    context = {
        'datas': datas,
    }

    return render(request, template, context)

def delete_angin(request, pk):

    template = 'inv/angin.html'
    Angin.objects.filter(id=pk).delete()

    datas = Angin.objects.all()

    context = {
        'datas': datas,
    }

    return render(request, template, context)

def delete_radiasi(request, pk):

    template = 'inv/radiasi.html'
    Radiasi.objects.filter(id=pk).delete()

    datas = Radiasi.objects.all()

    context = {
        'datas': datas,
    }

    return render(request, template, context)

#EXPORT ACTIONS LIST CSV
def export_parameters(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="parameter.csv"'
    writer = csv.writer(response)
    writer.writerow(['tanggal', 'jam0', 'jam1', 'jam2', 'jam3', 'jam4', 'jam5', 'jam6', 'jam7','jam8', 'jam9',
                    'jam10', 'jam11', 'jam12', 'jam13', 'jam14', 'jam15', 'jam16', 'jam17','jam18', 'jam19', 'jam20', 'jam21', 'jam22', 'jam23'])
    parameters = queryset.values_list('tanggal', 'jam0', 'jam1', 'jam2', 'jam3', 'jam4', 'jam5', 'jam6', 'jam7','jam8', 'jam9',
                    'jam10', 'jam11', 'jam12', 'jam13', 'jam14', 'jam15', 'jam16', 'jam17','jam18', 'jam19', 'jam20', 'jam21', 'jam22', 'jam23')
    for parameter in parameters:
        writer.writerow(parameter)
    return response
export_parameters.short_description = 'Export to csv'

#EXPORT ACTIONS LIST EXCEL

def export_excels(modeladmin, request, queryset):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename={date}-parameter.xls'.format(date=datetime.now().strftime('%Y-%m-%d'),)

    book = xlwt.Workbook(encoding='utf8')
    sheet = book.add_sheet('parameter')

    # Sheet header, first row

    # Sheet body, remaining rows
    default_style = xlwt.Style.default_style
    datetime_style = xlwt.easyxf(num_format_str='yyyy-mm-dd')
    date_style = xlwt.easyxf(num_format_str='yyyy-mm-dd')
    font_style = xlwt.easyxf('align: vert centre, horiz centre')

    rows = queryset.values_list('tanggal', 'jam0', 'jam1', 'jam2', 'jam3', 'jam4', 'jam5', 'jam6', 'jam7','jam8', 'jam9',
                'jam10', 'jam11', 'jam12', 'jam13', 'jam14', 'jam15', 'jam16', 'jam17','jam18', 'jam19', 'jam20', 'jam21', 'jam22', 'jam23')

    headers = ['Tanggal', 'Jam0', 'Jam1', 'Jam2', 'Jam3', 'Jam4', 'Jam5', 'Jam6', 'Jam7','Jam8', 'Jam9',
                'Jam10', 'Jam11', 'Jam12', 'Jam13', 'Jam14', 'Jam15', 'Jam16', 'Jam17','Jam18', 'Jam19', 'Jam20', 'Jam21', 'Jam22', 'Jam23']
    col_head = 0
    for head in headers:
        sheet.write(0, col_head, head, font_style)
        col_head += 1

#    for row in rows:
 #       row_num +=1
    for row, rowdata in enumerate(rows):
        for col, val in enumerate(rowdata):
#        for col_num in range(len(row)):
            if isinstance(val, datetime):
                style = datetime_style
            elif isinstance(val, date):
                style = date_style
            else:
                style = default_style
            
            sheet.write(row+1, col, val, style=style)

    book.save(response)
    return response

export_excels.short_description = 'Export to excel'

##EXPORT EXCEL CUSTOME RADIASI MATAHARI
def export_xlsx(modeladmin, request, queryset):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename={date}-parameter.xls'.format(date=datetime.now().strftime('%Y-%m-%d'),)

    book = xlwt.Workbook(encoding='utf8')
    sheet = book.add_sheet('parameter')

    # Sheet header, first row

    # Sheet body, remaining rows
    default_style = xlwt.Style.default_style
    datetime_style = xlwt.easyxf(num_format_str='yyyy-mm-dd')
    date_style = xlwt.easyxf(num_format_str='yyyy-mm-dd')
    font_style = xlwt.easyxf('align: vert centre, horiz centre')

    rows = queryset.values_list('tanggal', 'R_06_07', 'R_07_08', 'R_08_09', 'R_09_10', 'R_10_11', 'R_11_12', 'R_12_13', 'R_13_14','R_14_15', 'R_15_16',
                'R_16_17', 'R_17_18', 'R_18_19', 'R_19_20', 'R_20_21', 'R_21_22', 'R_22_23', 'R_23_00','R_00_01', 'R_01_02', 'R_02_03', 'R_03_04', 'R_04_05', 'R_05_06')

    headers = [
        'Tanggal', 'Radiasi 06-07','Radiasi 07-08','Radiasi 08-09','Radiasi 09-10','Radiasi 10-11','Radiasi 11-12','Radiasi 12-13','Radiasi 13-14','Radiasi 14-15','Radiasi 15-16','Radiasi 16-17','Radiasi 17-18',
        'Radiasi 18-19','Radiasi 19-20','Radiasi 20-21','Radiasi 21-22','Radiasi 22-23','Radiasi 23-00','Radiasi 00-01','Radiasi 01-02','Radiasi 02-03','Radiasi 03-04','Radiasi 04-05','Radiasi 05-06',
    ]

    col_head = 0
    for head in headers:
        sheet.write(0, col_head, head, font_style)
        col_head += 1

#    for row in rows:
 #       row_num +=1
    for row, rowdata in enumerate(rows):
        for col, val in enumerate(rowdata):
#        for col_num in range(len(row)):
            if isinstance(val, datetime):
                style = datetime_style
            elif isinstance(val, date):
                style = date_style
            else:
                style = default_style
            
            sheet.write(row+1, col, val, style=style)

    book.save(response)
    return response

export_xlsx.short_description = 'Export to excel'