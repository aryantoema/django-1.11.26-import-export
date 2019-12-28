from django import forms
from .models import *
#from django.contrib.auth.models import User

class KelembabanForm(forms.ModelForm):
	class Meta:
		model = Kelembaban
		fields = ('tanggal', 'jam0', 'jam1', 'jam2', 'jam3', 'jam4', 'jam5', 'jam6', 'jam7', 'jam8', 'jam9', 'jam10',
			'jam11', 'jam12', 'jam13', 'jam14', 'jam15', 'jam16', 'jam17', 'jam18', 'jam19', 'jam20', 'jam21', 'jam22',
			'jam23', )

class SuhuForm(forms.ModelForm):
	class Meta:
		model = Suhu
		fields = ('tanggal', 'jam0', 'jam1', 'jam2', 'jam3', 'jam4', 'jam5', 'jam6', 'jam7', 'jam8', 'jam9', 'jam10',
			'jam11', 'jam12', 'jam13', 'jam14', 'jam15', 'jam16', 'jam17', 'jam18', 'jam19', 'jam20', 'jam21', 'jam22',
			'jam23', )

class TekananForm(forms.ModelForm):
	class Meta:
		model = Tekanan
		fields = ('tanggal', 'jam0', 'jam1', 'jam2', 'jam3', 'jam4', 'jam5', 'jam6', 'jam7', 'jam8', 'jam9', 'jam10',
			'jam11', 'jam12', 'jam13', 'jam14', 'jam15', 'jam16', 'jam17', 'jam18', 'jam19', 'jam20', 'jam21', 'jam22',
			'jam23', )


#class DateInput(forms.DateInput):
#	input_type = 'date'

#class ExampleForm(forms.Form):
#	tanggal = forms.DateField(widget=DateInput)

class AnginForm(forms.ModelForm):
	class Meta:
		model = Angin
		fields = ('tanggal', 'jam0', 'jam1', 'jam2', 'jam3', 'jam4', 'jam5', 'jam6', 'jam7', 'jam8', 'jam9', 'jam10',
			'jam11', 'jam12', 'jam13', 'jam14', 'jam15', 'jam16', 'jam17', 'jam18', 'jam19', 'jam20', 'jam21', 'jam22',
			'jam23', )


class RadiasiForm(forms.ModelForm):
	class Meta:
		model = Radiasi
		fields = ('tanggal', 'R_06_07', 'R_07_08', 'R_08_09', 'R_09_10', 'R_10_11', 'R_11_12', 'R_12_13', 'R_13_14', 'R_14_15',
			'R_15_16', 'R_16_17', 'R_17_18', 'R_18_19', 'R_19_20', 'R_20_21', 'R_21_22', 'R_22_23', 'R_23_00', 'R_00_01', 'R_01_02', 'R_02_03', 'R_03_04', 'R_04_05', 'R_05_06',)