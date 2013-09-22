# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'Category', fields ['name_fr']
        db.delete_unique(u'projects_category', ['name_fr'])

        # Removing unique constraint on 'Category', fields ['name_en']
        db.delete_unique(u'projects_category', ['name_en'])

        # Removing unique constraint on 'Project', fields ['name_en']
        db.delete_unique(u'projects_project', ['name_en'])

        # Removing unique constraint on 'Project', fields ['name_fr']
        db.delete_unique(u'projects_project', ['name_fr'])


        # Changing field 'Project.link'
        db.alter_column(u'projects_project', 'link', self.gf('django.db.models.fields.URLField')(max_length=200, null=True))
        # Adding unique constraint on 'Project', fields ['slug']
        db.create_unique(u'projects_project', ['slug'])

        # Adding unique constraint on 'Category', fields ['slug']
        db.create_unique(u'projects_category', ['slug'])


    def backwards(self, orm):
        # Removing unique constraint on 'Category', fields ['slug']
        db.delete_unique(u'projects_category', ['slug'])

        # Removing unique constraint on 'Project', fields ['slug']
        db.delete_unique(u'projects_project', ['slug'])

        # Adding unique constraint on 'Project', fields ['name_fr']
        db.create_unique(u'projects_project', ['name_fr'])


        # Changing field 'Project.link'
        db.alter_column(u'projects_project', 'link', self.gf('django.db.models.fields.URLField')(default='', max_length=200))
        # Adding unique constraint on 'Project', fields ['name_en']
        db.create_unique(u'projects_project', ['name_en'])

        # Adding unique constraint on 'Category', fields ['name_en']
        db.create_unique(u'projects_category', ['name_en'])

        # Adding unique constraint on 'Category', fields ['name_fr']
        db.create_unique(u'projects_category', ['name_fr'])


    models = {
        u'projects.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'name_fr': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'})
        },
        u'projects.project': {
            'Meta': {'object_name': 'Project'},
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['projects.Category']", 'symmetrical': 'False'}),
            'cover': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime.now', 'db_index': 'True'}),
            'description_en': ('django.db.models.fields.TextField', [], {}),
            'description_fr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'images': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'name_fr': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'})
        }
    }

    complete_apps = ['projects']