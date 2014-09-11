# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Slider'
        db.create_table(u'administrador_slider', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('imagen', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('posicion', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('activo', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'administrador', ['Slider'])

        # Adding model 'Edecan'
        db.create_table(u'administrador_edecan', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('descripcion', self.gf('django.db.models.fields.TextField')()),
            ('imagen', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100)),
            ('sexo', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('activo', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'administrador', ['Edecan'])

        # Adding model 'Testimonial'
        db.create_table(u'administrador_testimonial', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cita', self.gf('django.db.models.fields.TextField')()),
            ('autor', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('puesto', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('activo', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'administrador', ['Testimonial'])


    def backwards(self, orm):
        # Deleting model 'Slider'
        db.delete_table(u'administrador_slider')

        # Deleting model 'Edecan'
        db.delete_table(u'administrador_edecan')

        # Deleting model 'Testimonial'
        db.delete_table(u'administrador_testimonial')


    models = {
        u'administrador.edecan': {
            'Meta': {'object_name': 'Edecan'},
            'activo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'descripcion': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'sexo': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        u'administrador.slider': {
            'Meta': {'object_name': 'Slider'},
            'activo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'posicion': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'administrador.testimonial': {
            'Meta': {'object_name': 'Testimonial'},
            'activo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'autor': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'cita': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'puesto': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        }
    }

    complete_apps = ['administrador']