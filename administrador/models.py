 # -*- coding: utf-8 -*-
from django.db import models
from sorl.thumbnail import ImageField

# Create your models here.

categorias = (
	('M', 'Masculino'),
	('F', 'Femenino'),
)

class Slider(models.Model):
	imagen = ImageField(upload_to = "sliders")
	titulo = models.CharField(max_length=45,blank=True)
	descripcion = models.CharField(max_length=45,blank=True)
	posicion = models.IntegerField(default = 1)
	activo = models.BooleanField(default=True)

	def __str__(self):
		return self.titulo

class Edecan(models.Model):
	class Meta:
		verbose_name_plural = "Edecanes"

	nombre = models.CharField(max_length=60)
	descripcion = models.TextField(blank=True)
	imagen = ImageField(upload_to = "edecanes")
	sexo = models.CharField(max_length=1, choices=categorias)
	activo = models.BooleanField(default=True)

	def __str__(self):
		return self.nombre

class Testimonial(models.Model):
	class Meta:
		verbose_name_plural = "Testimoniales"
	cita = models.TextField()
	autor = models.CharField(max_length=60,blank=True)
	puesto = models.CharField(max_length=60,blank=True)
	activo = models.BooleanField(default=True)
	
	def __str__(self):
		return self.cita