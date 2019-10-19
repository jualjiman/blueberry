from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.contrib.sitemaps import views as sitemaps_views
from django.views import static

from blueberry.sitemaps import HomeStaticViewSitemap, OtherStaticViewSitemap
from administrador import views

admin.autodiscover()

sitemaps_options = {"home": HomeStaticViewSitemap, "other": OtherStaticViewSitemap}

urlpatterns = [
    url(r"^admin/", admin.site.urls),
    url(r"^$", views.home, name="home"),
    url(r"^nosotros/$", views.nosotros, name="nosotros"),
    url(r"^servicios/$", views.servicios, name="servicios"),
    url(r"^eventos/$", views.eventos, name="eventos"),
    url(r"^book/$", views.book, name="book"),
    url(r"^contacto/$", views.contacto, name="contacto"),
    url(r"^contactame/$", views.contactame, name="contactame"),
    url(r"^mas/$", views.mas, name="mas"),
    url(r"^sitemap\.xml$", sitemaps_views.sitemap, {"sitemaps": sitemaps_options}),
    url(
        r"^webapps/fortalezac/fortaleza/media/(?P<path>.*)$",
        static.serve,
        {"document_root": settings.MEDIA_ROOT},
    ),
    url(
        r"^static/(?P<path>.*)$",
        static.serve,
        {"document_root": settings.STATIC_ROOT, "show_indexes": True},
    ),
    url(
        r"^media/(?P<path>.*)$",
        static.serve,
        {"document_root": settings.MEDIA_ROOT, "show_indexes": True},
    ),
]
