# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Slider.descripcion'
        db.alter_column(u'administrador_slider', 'descripcion', self.gf('django.db.models.fields.CharField')(max_length=45))

        # Changing field 'Slider.titulo'
        db.alter_column(u'administrador_slider', 'titulo', self.gf('django.db.models.fields.CharField')(max_length=45))

    def backwards(self, orm):

        # Changing field 'Slider.descripcion'
        db.alter_column(u'administrador_slider', 'descripcion', self.gf('django.db.models.fields.CharField')(max_length=30))

        # Changing field 'Slider.titulo'
        db.alter_column(u'administrador_slider', 'titulo', self.gf('django.db.models.fields.CharField')(max_length=30))

    models = {
        u'administrador.edecan': {
            'Meta': {'object_name': 'Edecan'},
            'activo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'descripcion': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'sexo': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        u'administrador.slider': {
            'Meta': {'object_name': 'Slider'},
            'activo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '45', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'posicion': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '45', 'blank': 'True'})
        },
        u'administrador.testimonial': {
            'Meta': {'object_name': 'Testimonial'},
            'activo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'autor': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True'}),
            'cita': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'puesto': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True'})
        }
    }

    complete_apps = ['administrador']