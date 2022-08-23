import pymongo
import pandas as pd
from io import BytesIO

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import DocumentForm
from .models import Data

def home(request):
	return render(request, 'data_visualizer/html/main.html')


def insertar(request):
	if request.method == 'POST':

		form = DocumentForm(request.POST, request.FILES)

		
		excel_file = request.FILES['myfile']
		data = get_info_excel(excel_file)
		data.save()

		return redirect('confirmation')

	return render(request, 'data_visualizer/html/cadastro.html')

def confirmation(request):

	if request.method == 'POST':
		if 'confirmar' in request.POST:
			return redirect('dados_pacient', pacient=data.apellido)

		elif 'cancelar' in request.POST:
			return redirect('insertar')
	
	return render(request, 'data_visualizer/html/confirmation.html')

def consulta(request):
	pass


def dados(visualizer):
	pass


def dados_pacient(request, pacient):
	pass


def get_info_excel(excel_file):

	df1 = pd.read_excel(exel_file, sheet_name=0, header=None)

	df2 = pd.read_excel(exel_file, sheet_name=1, header=None)

	list_pie_e_x = []
	list_pie_e_y = []

	list_pie_d_x = []
	list_pie_d_y = []

	list_pression_e = []
	list_pression_d = []

	list_tiempo = []

	for x in range(16, 256):
		list_tiempo.append(df2.iloc[x][1])
		list_pression_e.append(df2.iloc[x][2])
		list_pression_d.append(df2.iloc[x][4])

	for x in range(16, 95):
		list_pie_e_x.append(df1.iloc[x][1])
		list_pie_e_y.append(df1.iloc[x][2])

	for x in range(96, 140):
		list_pie_e_x.append(df1.iloc[x][5])
		list_pie_e_y.append(df1.iloc[x][6])

	for x in range(16, 140):
		list_pie_d_x.append(df1.iloc[x][3])
		list_pie_d_y.append(df1.iloc[x][4])	
					
	data = Data()

	data.apellido = df1.iloc[0][1]
	data.nombre = df1.iloc[1][1]
	data.edad = df1.iloc[2][1]
	data.altura = df1.iloc[3][1]
	data.n_de_pie = df1.iloc[4][1]
	data.peso = df1.iloc[5][1]
	data.duracion = df1.iloc[6][1]
	data.frecuencia = df1.iloc[7][1]

	data.list_tiempo = ','.join(str(x) for x in list_tiempo)
	data.list_pie_e_x = ','.join(str(x) for x in list_pie_e_x)
	data.list_pie_e_y = ','.join(str(x) for x in list_pie_e_y)
	data.list_pression_e = ','.join(str(x) for x in list_pression_e)
	data.list_pie_d_x = ','.join(str(x) for x in list_pie_d_x)
	data.list_pie_d_y = ','.join(str(x) for x in list_pie_d_y)
	data.list_pression_d = ','.join(str(x) for x in list_pression_d)

	return data