from django.contrib import admin
from .models import *
from sorl.thumbnail.shortcuts import get_thumbnail

# Register your models here.


class SliderAdmin(admin.ModelAdmin):
    list_display = ('imagen_slider', 'titulo', 'descripcion', 'activo',)
    search_fields = ['titulo', 'descripcion', ]

    def imagen_slider(self, obj):
        return '<img src="%s" />' % get_thumbnail(obj.imagen, '100x60', crop='center').url

    imagen_slider.allow_tags = True


class EventoAdmin(admin.ModelAdmin):
    list_display = (
        'imagen_evento', 'lugar', 'servicio', 'posicion', 'activo',
    )
    search_fields = ['lugar', 'servicio', ]

    def imagen_evento(self, obj):
        return '<img src="%s" />' % get_thumbnail(obj.imagen, '100x60', crop='center').url

    imagen_evento.allow_tags = True


class EdecanAdmin(admin.ModelAdmin):
    list_display = ('imagen_edecan', 'activo', 'prioridad', 'alineacion',)

    def imagen_edecan(self, obj):
        return '<img src="%s" />' % get_thumbnail(obj.imagen, '100x100', crop='center').url

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs

    imagen_edecan.allow_tags = True


class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('cita', 'autor', 'puesto', 'activo',)
    search_fields = ['cita', 'autor', 'puesto']


class MensAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'mensaje', 'fecha')


class Messages(admin.ModelAdmin):
    list_display = ('sender', 'recipient', 'subject', 'nattachments', 'fecha')


admin.site.register(Mensaje, MensAdmin)
admin.site.register(Email, Messages)
admin.site.register(Slider, SliderAdmin)
admin.site.register(Evento, EventoAdmin)
admin.site.register(Edecan, EdecanAdmin)
admin.site.register(Testimonial, TestimonialAdmin)
