# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Mensaje'
        db.create_table(u'administrador_mensaje', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('subject', self.gf('django.db.models.fields.TextField')()),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('mensaje', self.gf('django.db.models.fields.TextField')()),
            ('fecha', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 12, 30, 0, 0))),
        ))
        db.send_create_signal(u'administrador', ['Mensaje'])

        # Adding model 'Evento'
        db.create_table(u'administrador_evento', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('imagen', self.gf(u'sorl.thumbnail.fields.ImageField')(max_length=100)),
            ('lugar', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('servicio', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('posicion', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('activo', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'administrador', ['Evento'])

        # Adding model 'Email'
        db.create_table(u'administrador_email', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sender', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('recipient', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('subject', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('body', self.gf('django.db.models.fields.TextField')()),
            ('nattachments', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('fecha', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 12, 30, 0, 0))),
        ))
        db.send_create_signal(u'administrador', ['Email'])


    def backwards(self, orm):
        # Deleting model 'Mensaje'
        db.delete_table(u'administrador_mensaje')

        # Deleting model 'Evento'
        db.delete_table(u'administrador_evento')

        # Deleting model 'Email'
        db.delete_table(u'administrador_email')


    models = {
        u'administrador.edecan': {
            'Meta': {'object_name': 'Edecan'},
            'activo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'descripcion': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': (u'sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'prioridad': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'sexo': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        u'administrador.email': {
            'Meta': {'object_name': 'Email'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'fecha': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 12, 30, 0, 0)'}),
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
            'lugar': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'posicion': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'servicio': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'administrador.mensaje': {
            'Meta': {'object_name': 'Mensaje'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'fecha': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 12, 30, 0, 0)'}),
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