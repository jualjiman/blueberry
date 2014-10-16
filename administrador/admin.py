from django.contrib import admin
from .models import *
from sorl.thumbnail.shortcuts import get_thumbnail

# Register your models here.

class SliderAdmin(admin.ModelAdmin):
	list_display = ('imagen_slider','titulo','descripcion','activo',)
	search_fields = ['titulo','descripcion',]

	def imagen_slider(self,obj):
		return '<img src="%s" />' % get_thumbnail(obj.imagen,'100x60', crop='center').url #format='PNG', quality=99

	imagen_slider.allow_tags = True

class EventoAdmin(admin.ModelAdmin):
	list_display = ('imagen_evento','lugar','servicio','posicion','activo',)
	search_fields = ['lugar','servicio',]

	def imagen_evento(self,obj):
		return '<img src="%s" />' % get_thumbnail(obj.imagen,'100x60', crop='center').url #format='PNG', quality=99

	imagen_evento.allow_tags = True

class EdecanAdmin(admin.ModelAdmin):
	list_display = ('imagen_edecan','nombre','activo','prioridad','sexo',)
	search_fields = ['nombre','descripcion',]

	def imagen_edecan(self,obj):
		return '<img src="%s" />' % get_thumbnail(obj.imagen,'100x100', crop='center').url #format='PNG', quality=99

	imagen_edecan.allow_tags = True

class TestimonialAdmin(admin.ModelAdmin):
	list_display = ('cita','autor','puesto','activo',)
	search_fields = ['cita','autor','puesto']

admin.site.register(Slider,SliderAdmin)
admin.site.register(Evento,EventoAdmin)
admin.site.register(Edecan,EdecanAdmin)
admin.site.register(Testimonial,TestimonialAdmin)
