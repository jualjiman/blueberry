from django.conf import settings
from django.conf.urls import include, patterns, url
from django.contrib import admin

from blueberry.sitemaps import HomeStaticViewSitemap, OtherStaticViewSitemap

admin.autodiscover()

sitemaps = {
    'home': HomeStaticViewSitemap,
    'other': OtherStaticViewSitemap
}

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'administrador.views.home', name='home'),
    url(r'^nosotros/$', 'administrador.views.nosotros', name='nosotros'),
    url(r'^servicios/$', 'administrador.views.servicios', name='servicios'),
    url(r'^eventos/$', 'administrador.views.eventos', name='eventos'),
    url(r'^book/$', 'administrador.views.book', name='book'),
    url(r'^contacto/$', 'administrador.views.contacto', name='contacto'),
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps})
)

urlpatterns += patterns('',url(r'^/webapps/fortalezac/fortaleza/media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,}),)
urlpatterns += patterns('',(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT, 'show_indexes':True}),)
urlpatterns += patterns('',(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes':True}),)
