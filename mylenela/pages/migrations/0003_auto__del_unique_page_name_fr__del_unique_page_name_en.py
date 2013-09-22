# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'Page', fields ['name_en']
        db.delete_unique(u'pages_page', ['name_en'])

        # Removing unique constraint on 'Page', fields ['name_fr']
        db.delete_unique(u'pages_page', ['name_fr'])


    def backwards(self, orm):
        # Adding unique constraint on 'Page', fields ['name_fr']
        db.create_unique(u'pages_page', ['name_fr'])

        # Adding unique constraint on 'Page', fields ['name_en']
        db.create_unique(u'pages_page', ['name_en'])


    models = {
        u'pages.page': {
            'Meta': {'object_name': 'Page'},
            'content_en': ('django.db.models.fields.TextField', [], {}),
            'content_fr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'name_fr': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'})
        }
    }

    complete_apps = ['pages']