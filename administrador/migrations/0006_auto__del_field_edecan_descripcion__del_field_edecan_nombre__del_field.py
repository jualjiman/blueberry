# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Edecan.descripcion'
        db.delete_column(u'administrador_edecan', 'descripcion')

        # Deleting field 'Edecan.nombre'
        db.delete_column(u'administrador_edecan', 'nombre')

        # Deleting field 'Edecan.sexo'
        db.delete_column(u'administrador_edecan', 'sexo')

        # Adding field 'Edecan.alineacion'
        db.add_column(u'administrador_edecan', 'alineacion',
                      self.gf('django.db.models.fields.CharField')(default='center', max_length=6),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Edecan.descripcion'
        db.add_column(u'administrador_edecan', 'descripcion',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Edecan.nombre'
        db.add_column(u'administrador_edecan', 'nombre',
                      self.gf('django.db.models.fields.CharField')(max_length=60, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Edecan.sexo'
        db.add_column(u'administrador_edecan', 'sexo',
                      self.gf('django.db.models.fields.CharField')(default='center', max_length=1),
                      keep_default=False)

        # Deleting field 'Edecan.alineacion'
        db.delete_column(u'administrador_edecan', 'alineacion')


    models = {
        u'administrador.edecan': {
            'Meta': {'object_name': 'Edecan'},
            'activo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'alineacion': ('django.db.models.fields.CharField', [], {'default': "'center'", 'max_length': '6'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': (u'sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'prioridad': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        },
        u'administrador.email': {
            'Meta': {'object_name': 'Email'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'fecha': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2019, 9, 26, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nattachments': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'recipient': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'sender': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'administrador.evento': {
            'Meta': {'object_name': 'Evento'},
            'activo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': (u'sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'lugar': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'posicion': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'servicio': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'administrador.mensaje': {
            'Meta': {'object_name': 'Mensaje'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'fecha': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2019, 9, 26, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mensaje': ('django.db.models.fields.TextField', [], {}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'subject': ('django.db.models.fields.TextField', [], {})
        },
        u'administrador.slider': {
            'Meta': {'object_name': 'Slider'},
            'activo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '45', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': (u'sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
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
