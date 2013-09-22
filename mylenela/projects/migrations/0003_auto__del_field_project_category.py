# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Project.category'
        db.delete_column(u'projects_project', 'category_id')

        # Adding M2M table for field categories on 'Project'
        m2m_table_name = db.shorten_name(u'projects_project_categories')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm[u'projects.project'], null=False)),
            ('category', models.ForeignKey(orm[u'projects.category'], null=False))
        ))
        db.create_unique(m2m_table_name, ['project_id', 'category_id'])


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Project.category'
        raise RuntimeError("Cannot reverse this migration. 'Project.category' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Project.category'
        db.add_column(u'projects_project', 'category',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['projects.Category']),
                      keep_default=False)

        # Removing M2M table for field categories on 'Project'
        db.delete_table(db.shorten_name(u'projects_project_categories'))


    models = {
        u'projects.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'name_fr': ('django.db.models.fields.CharField', [], {'max_length': '50', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100'})
        },
        u'projects.project': {
            'Meta': {'object_name': 'Project'},
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['projects.Category']", 'symmetrical': 'False'}),
            'cover': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'date': ('django.db.models.fields.DateField', [], {'db_index': 'True'}),
            'description_en': ('django.db.models.fields.TextField', [], {}),
            'description_fr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'images': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'name_fr': ('django.db.models.fields.CharField', [], {'max_length': '50', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['projects']