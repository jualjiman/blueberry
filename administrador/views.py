from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .models import *

#from .forms import *

# Create your views here.

def home(request):
	sliders = Slider.objects.filter(activo = True)
	testimoniales = Testimonial.objects.filter(activo = True)
	edecanes = Edecan.objects.filter(activo = True)[:8]

	return render(request,"index.html",{"sliders": sliders, "testimoniales":testimoniales,"edecanes":edecanes,})

def nosotros(request):
	return render(
		request,
		"nosotros.html",
		{}
	)

def servicios(request):
	testimoniales = Testimonial.objects.filter(activo = True)
	return render(
		request,
		"servicios.html",
		{
			"testimoniales":testimoniales,
		}
	)

def book(request):
	testimoniales = Testimonial.objects.filter(activo = True)
	edecanes = Edecan.objects.filter(activo = True).order_by("nombre")[:8]

	return render(
		request,
		"book.html",
		{
			"testimoniales":testimoniales,
			"edecanes":edecanes,
		}
	)

def contacto(request):
	return render(
		request,
		"contacto.html",
		{}
	)

@csrf_exempt
def mas(request):
	if request.is_ajax():
	    pagina = int(request.POST['num'])
	    pagina *= 8

	    otros = Edecan.objects.filter(activo = True).order_by("nombre")[pagina:(pagina+8)]

	    return render(request,"mas.html",{"otros": otros})
	else:
		return HttpResponseRedirect("/")