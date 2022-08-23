from django.db import models

class Document(models.Model):
    document = models.FileField(upload_to='images/')

class Data(models.Model):
	apellido = models.CharField(max_length=200)
	nombre = models.CharField(max_length=200)
	edad = models.IntegerField()
	altura = models.IntegerField()
	n_de_pie = models.IntegerField()
	peso = models.IntegerField()
	duracion = models.IntegerField()
	frecuencia = models.IntegerField()
	list_tiempo = models.CharField(max_length=20000)
	list_pie_e_x = models.CharField(max_length=20000)
	list_pie_e_y = models.CharField(max_length=20000)
	list_pression_e = models.CharField(max_length=20000)
	list_pie_d_x = models.CharField(max_length=20000)
	list_pie_d_y = models.CharField(max_length=20000)
	list_pression_d = models.CharField(max_length=20000)