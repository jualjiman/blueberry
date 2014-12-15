from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .models import *
from random import sample

#from .forms import *

# Create your views here.

def home(request):
	sliders = Slider.objects.filter(activo = True)
	testimoniales = Testimonial.objects.filter(activo = True)
	edecanes = Edecan.objects.filter(activo = True).order_by("prioridad")[:8]
	titulo = "Home"

	return render(request,"index.html",{"sliders": sliders, "testimoniales":testimoniales,"edecanes":edecanes,"titulo":titulo,})

def nosotros(request):
	titulo = "Nosotros"
	return render(
		request,
		"nosotros.html",
		{
			"titulo":titulo,
		}
	)

def servicios(request):
	testimoniales = Testimonial.objects.filter(activo = True)
	titulo = "Servicios"
	return render(
		request,
		"servicios.html",
		{
			"testimoniales":testimoniales,
			"titulo":titulo,
		}
	)

def eventos(request):
        eventos = Evento.objects.filter(activo = True)
        titulo = "Eventos"
        return render(
                request,
                "eventos.html",
                {
                        "eventos":eventos,
                        "titulo":titulo,
                }
        )

def book(request):
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
		}
	)

def contacto(request):
	titulo = "Contacto"
	return render(
		request,
		"contacto.html",
		{
			"titulo":titulo,
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
