# -*- coding: utf-8 -*-
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .models import *
from .forms import *
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt


def home(request):
    keywords = (
        u'edecanes en Acapulco, gios, pasarelas, desfiles, campañas, '
        u'exposiciones, promociones, convenciones, animación, eventos'
    )
    description = (
        u'Servicio 100% profesional, Amplia y Exitosa '
        u'experiencia: Congresos, Convenciones, Exposiciones, Campañas '
        u'BTL etc. Móvil: 744 588 4304'
    )
    sliders = Slider.objects.filter(activo=True)
    testimoniales = Testimonial.objects.filter(activo=True)
    edecanes = Edecan.objects.filter(activo=True).order_by("prioridad")[:8]

    form = ContactForm()
    return render(
        request,
        "index.html",
        {
            "sliders": sliders,
            "testimoniales": testimoniales,
            "edecanes": edecanes,
            "keywords": keywords,
            "description": description,
            "form": form
        }
    )


def nosotros(request):
    keywords = (
        u'edecanes en Acapulco, gios, pasarelas, desfiles, campañas, '
        u'exposiciones, promociones, convenciones, animación, eventos'
    )
    description = (
        u'Blueberry es una Agencia de Edecanes que tiene como objetivo '
        u'principal contribuir a mejorar la imagen de marca y calidad de '
        u'negocio de nuestros clientes.'
    )

    form = ContactForm()
    return render(
        request,
        "nosotros.html",
        {
            "keywords": keywords,
            "description": description,
            "form": form
        }
    )


def servicios(request):
    keywords = (
        u'edecanes en Acapulco, gios, pasarelas, desfiles, campañas, '
        u'exposiciones, promociones, convenciones, animación, eventos'
    )
    description = (
        u'Contrata a nuestros profesionales para: pasarelas, desfiles '
        u'de moda, campañas, exposiciones, lanzamiento y '
        u'reposicionamiento de productos, promociones, convenciones, etc.'
    )
    testimoniales = Testimonial.objects.filter(activo=True)

    form = ContactForm()
    return render(
        request,
        "servicios.html",
        {
            "testimoniales": testimoniales,
            "keywords": keywords,
            "description": description,
            "form": form
        }
    )


def eventos(request):
    keywords = (
        u'edecanes en Acapulco, gios, pasarelas, desfiles, '
        u'campañas, exposiciones, promociones, convenciones, animación, '
        u'eventos'
    )
    description = (
        u'Congresos, Convenciones, Exposiciones, Ferias, Muestreo, '
        u'Encuestas, Pasarelas, Campañas de lanzamiento, Siembra de '
        u'Productos, Posicionamiento de marca, Campañas BTL'
    )
    eventos = Evento.objects.filter(activo=True).order_by("-posicion")

    form = ContactForm()
    return render(
        request,
        "eventos.html",
        {
            "eventos": eventos,
            "keywords": keywords,
            "description": description,
            "form": form
        }
    )


def book(request):
    keywords = (
        u'edecanes en Acapulco, gios, pasarelas, desfiles, campañas, '
        u'exposiciones, promociones, convenciones, animación, eventos'
    )
    description = (
        u'Ofrecemos un servicio 100% profesional, nuestras edecanes '
        u'tienen una excelente presentación, así como actitud de servicio '
        u'para representar a su empresa en forma por demás profesional.'
    )
    testimoniales = Testimonial.objects.filter(activo=True)
    edecanes = Edecan.objects.filter(activo=True).order_by("prioridad")[:20]

    form = ContactForm()
    return render(
        request,
        "book.html",
        {
            "testimoniales": testimoniales,
            "edecanes": edecanes,
            "keywords": keywords,
            "description": description,
            "form": form
        }
    )


def contacto(request):
    keywords = (
        u'edecanes en Acapulco, gios, pasarelas, desfiles, campañas, '
        u'exposiciones, promociones, convenciones, animación, eventos'
    )
    description = (
        u'Nos encargarnos de la organización total de tu evento así '
        u'como también de todos los servicios y equipamientos que necesites.'
    )

    form = ContactForm()
    return render(
        request,
        "contacto.html",
        {
            "keywords": keywords,
            "description": description,
            "form": form
        }
    )


@csrf_exempt
def mas(request):
    if request.is_ajax():
        pagina = (int(request.POST['num']) + 4) * 4

        otros = Edecan.objects.filter(
            activo=True
        ).order_by(
            "prioridad"
        )[pagina:(pagina+4)]

        return render(
            request,
            "mas.html",
            {
                "otros": otros
            }
        )
    else:
        return HttpResponseRedirect("/")


def contactame(request):
    if request.is_ajax():
        nombre = request.POST['name']
        email = request.POST['email']
        mensaje = request.POST['message']
        asunto = request.POST['subject']

        dfrom = nombre + " <" + email + ">"
        mensaje = "\n" + "Asunto: " + asunto + "\n" + dfrom + "\n\n" + mensaje

        send_mail(
            'Mensaje desde Edecanes en Acapulco',
            mensaje,
            "Blueberry's mailer <mailer@edecanesenacapulco.com.mx>",
            ['contacto@edecanesenacapulco.com.mx', ],
            fail_silently=False
        )
        msj = Mensaje(nombre=dfrom, email=email, mensaje=mensaje)
        msj.save()

        return HttpResponse('Ok')
    else:
            home(request)


# Handler for HTTP POST to http://myhost.com/messages
# for the route defined above
@csrf_exempt
def messages(request):
    if request.method == 'POST':
        sender = request.POST.get('sender')
        recipient = request.POST.get('recipient')
        subject = request.POST.get('subject', '')

        body_without_quotes = request.POST.get('stripped-text', '')
        # note: other MIME headers are also posted here...

        nattachments = 0
        # attachments:
        for key in request.FILES:
            nattachments += 1
        # do something with the file

        msg = Email(
            sender=sender,
            recipient=recipient,
            subject=subject,
            body=body_without_quotes,
            nattachments=nattachments
        )
        msg.save()

    # Returned text is ignored but HTTP status code matters:
    # Mailgun wants to see 2xx, otherwise it will make another attempt
    # in 5 minutes
    return HttpResponse('OK')
