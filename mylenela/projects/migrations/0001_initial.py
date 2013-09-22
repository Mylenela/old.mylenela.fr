# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Image'
        db.create_table(u'projects_image', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal(u'projects', ['Image'])

        # Adding model 'Category'
        db.create_table(u'projects_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name_en', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('name_fr', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=100)),
        ))
        db.send_create_signal(u'projects', ['Category'])

        # Adding model 'Project'
        db.create_table(u'projects_project', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name_en', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('name_fr', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=100)),
            ('description_en', self.gf('django.db.models.fields.TextField')()),
            ('description_fr', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime.now, db_index=True)),
            ('cover', self.gf('django.db.models.fields.related.ForeignKey')(related_name='cover', to=orm['projects.Image'])),
        ))
        db.send_create_signal(u'projects', ['Project'])

        # Adding M2M table for field categories on 'Project'
        m2m_table_name = db.shorten_name(u'projects_project_categories')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm[u'projects.project'], null=False)),
            ('category', models.ForeignKey(orm[u'projects.category'], null=False))
        ))
        db.create_unique(m2m_table_name, ['project_id', 'category_id'])

        # Adding M2M table for field images on 'Project'
        m2m_table_name = db.shorten_name(u'projects_project_images')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm[u'projects.project'], null=False)),
            ('image', models.ForeignKey(orm[u'projects.image'], null=False))
        ))
        db.create_unique(m2m_table_name, ['project_id', 'image_id'])


    def backwards(self, orm):
        # Deleting model 'Image'
        db.delete_table(u'projects_image')

        # Deleting model 'Category'
        db.delete_table(u'projects_category')

        # Deleting model 'Project'
        db.delete_table(u'projects_project')

        # Removing M2M table for field categories on 'Project'
        db.delete_table(db.shorten_name(u'projects_project_categories'))

        # Removing M2M table for field images on 'Project'
        db.delete_table(db.shorten_name(u'projects_project_images'))


    models = {
        u'projects.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'name_fr': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'})
        },
        u'projects.image': {
            'Meta': {'object_name': 'Image'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        },
        u'projects.project': {
            'Meta': {'object_name': 'Project'},
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['projects.Category']", 'symmetrical': 'False'}),
            'cover': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'cover'", 'to': u"orm['projects.Image']"}),
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime.now', 'db_index': 'True'}),
            'description_en': ('django.db.models.fields.TextField', [], {}),
            'description_fr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'images': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'images'", 'symmetrical': 'False', 'to': u"orm['projects.Image']"}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'name_fr': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'})
        }
    }

    complete_apps = ['projects']