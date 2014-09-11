from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blueberry.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'administrador.views.home', name='home'),
    url(r'^nosotros/$', 'administrador.views.nosotros', name='nosotros'),
    url(r'^servicios/$', 'administrador.views.servicios', name='servicios'),
    url(r'^book/$', 'administrador.views.book', name='book'),
    url(r'^contacto/$', 'administrador.views.contacto', name='contacto'),
    url(r'^mas/$', 'administrador.views.mas', name='mas'),
)

urlpatterns += patterns('',url(r'^/webapps/fortalezac/fortaleza/media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,}),)
urlpatterns += patterns('',(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT, 'show_indexes':True}),)
urlpatterns += patterns('',(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes':True}),)
