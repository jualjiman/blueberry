# -*- coding: utf-8 -*-
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .models import *
from random import sample

#from .forms import *

# Create your views here.

def home(request):
	keywords = u"edecanes, acapulco, gios, pasarelas, desfiles, campañas, exposiciones, lanzamientos, promociones, convenciones, animación, evento, profesional, presentación"
	description = "Ofrecemos un servicio 100% profesional, nuestras edecanes tienen una excelente presentación, así como actitud de servicio para representar a su empresa en forma por demás profesional."
	sliders = Slider.objects.filter(activo = True)
	testimoniales = Testimonial.objects.filter(activo = True)
	edecanes = Edecan.objects.filter(activo = True).order_by("prioridad")[:8]
	titulo = "Home"

	return render(
		request,
		"index.html",
		{
			"sliders": sliders, 
			"testimoniales":testimoniales,
			"edecanes":edecanes,
			"titulo":titulo,
			"keywords":keywords,
			"description":description,
		}
	)

def nosotros(request):
	keywords = u"edecanes, acapulco, gios, pasarelas, desfiles, campañas, exposiciones, lanzamientos, promociones, convenciones, animación, evento, profesional, presentación"
	description = "Blueberry es una Agencia de Edecanes que tiene como objetivo principal contribuir a mejorar la imagen de marca y calidad de negocio de nuestros clientes."
	titulo = "Nosotros"
	return render(
		request,
		"nosotros.html",
		{
			"titulo":titulo,
			"keywords":keywords,
			"description":description,
		}
	)

def servicios(request):
	keywords = u"edecanes, acapulco, gios, pasarelas, desfiles, campañas, exposiciones, lanzamientos, promociones, convenciones, animación, evento, profesional, presentación"
	description = "Contrata a nuestros profesionales para: pasarelas, desfiles de moda, campañas, exposiciones, lanzamiento y reposicionamiento de productos, promociones, convenciones, etc."
	testimoniales = Testimonial.objects.filter(activo = True)
	titulo = "Servicios"
	return render(
		request,
		"servicios.html",
		{
			"testimoniales":testimoniales,
			"titulo":titulo,
			"keywords":keywords,
			"description":description,
		}
	)

def eventos(request):
	keywords = u"edecanes, acapulco, gios, pasarelas, desfiles, campañas, exposiciones, lanzamientos, promociones, convenciones, animación, evento, profesional, presentación"
	description = "Congresos, Convenciones, Exposiciones, Ferias, Muestreo, Encuestas, Pasarelas, Campañas de lanzamiento, Siembra de Productos, Posicionamiento de marca, Campañas BTL"
        eventos = Evento.objects.filter(activo = True)
        titulo = "Eventos"
        return render(
                request,
                "eventos.html",
                {
                    "eventos":eventos,
                    "titulo":titulo,
                    "keywords":keywords,
					"description":description,
                }
        )

def book(request):
	keywords = u"edecanes, acapulco, gios, pasarelas, desfiles, campañas, exposiciones, lanzamientos, promociones, convenciones, animación, evento, profesional, presentación"
	description = "Ofrecemos un servicio 100% profesional, nuestras edecanes tienen una excelente presentación, así como actitud de servicio para representar a su empresa en forma por demás profesional."
	testimoniales = Testimonial.objects.filter(activo = True)
	edecanes = Edecan.objects.filter(activo = True).order_by("prioridad")[:8]
	titulo = "Book"

	return render(
		request,
		"book.html",
		{
			"testimoniales":testimoniales,
			"titulo":titulo,
			"edecanes":edecanes,
			"keywords":keywords,
			"description":description,
		}
	)

def contacto(request):
	keywords = u"edecanes, acapulco, gios, pasarelas, desfiles, campañas, exposiciones, lanzamientos, promociones, convenciones, animación, evento, profesional, presentación"
	description = "Nos encargarnos de la organización total de tu evento así como también de todos los servicios y equipamientos que necesites."
	titulo = "Contacto"
	return render(
		request,
		"contacto.html",
		{
			"titulo":titulo,
			"keywords":keywords,
			"description":description,
		}
	)

@csrf_exempt
def mas(request):
	if request.is_ajax():
	    pagina = int(request.POST['num'])
	    pagina *= 8

	    otros = Edecan.objects.filter(activo = True).order_by("prioridad")[pagina:(pagina+8)]

	    return render(request,"mas.html",{"otros": otros})
	else:
		return HttpResponseRedirect("/")
