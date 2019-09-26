 # -*- coding: utf-8 -*-
from datetime import date, datetime

from django.db import models
from sorl.thumbnail import ImageField

# Create your models here.

alineaciones = (
    ('top', 'Arriba'),
    ('center', 'Centrado'),
    ('bottom', 'Abajo'),
)


class Slider(models.Model):
    imagen = ImageField(upload_to="sliders")
    titulo = models.CharField(max_length=45, blank=True)
    descripcion = models.CharField(max_length=45, blank=True)
    posicion = models.IntegerField(default=1)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo


class Evento(models.Model):
    imagen = ImageField(upload_to="eventos")
    lugar = models.CharField(max_length=60, blank=True, null=True)
    servicio = models.CharField(max_length=100, blank=True, null=True)
    posicion = models.IntegerField(default=1)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.lugar


class Edecan(models.Model):
    class Meta:
        verbose_name_plural = "Edecanes"

    imagen = ImageField(upload_to="edecanes")
    alineacion = models.CharField(max_length=6, choices=alineaciones, default='center')
    prioridad = models.IntegerField(default=1)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return str(self.id)


class Testimonial(models.Model):
    class Meta:
        verbose_name_plural = "Testimoniales"
    cita = models.TextField()
    autor = models.CharField(max_length=60, blank=True)
    puesto = models.CharField(max_length=60, blank=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.cita


class Mensaje(models.Model):
    nombre = models.CharField(max_length=100)
    subject = models.TextField()
    email = models.EmailField()
    mensaje = models.TextField()
    fecha = models.DateTimeField(default=datetime.now(), editable=False)

    def __str__(self):
        return self.nombre


class Email(models.Model):
    sender = models.CharField(max_length=150)
    recipient = models.CharField(max_length=150)
    subject = models.CharField(max_length=200)
    body = models.TextField()
    nattachments = models.IntegerField(default=0)
    fecha = models.DateTimeField(default=datetime.now(), editable=False)

    def __str__(self):
        return self.sender
