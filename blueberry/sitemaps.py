from datetime import datetime

from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class StaticViewSitemap(Sitemap):
    def location(self, item):
        return reverse(item)

    def lastmod(self, item):
            return datetime(2019, 1, 1, 1, 1, 1)


class OtherStaticViewSitemap(StaticViewSitemap):
    priority = 0.8

    def items(self):
        return [
            'nosotros',
            'servicios',
            'eventos',
            'book',
            'contacto'
        ]


class HomeStaticViewSitemap(StaticViewSitemap):
    priority = 1.0

    def items(self):
        return ['home']
