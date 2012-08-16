# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Tags.icon'
        db.add_column('pattern_tags', 'icon',
                      self.gf('django.db.models.fields.URLField')(default='http://', max_length=200),
                      keep_default=False)

    def backwards(self, orm):
        # Deleting field 'Tags.icon'
        db.delete_column('pattern_tags', 'icon')

    models = {
        'pattern.implementation': {
            'Meta': {'object_name': 'Implementation'},
            'gist': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pattern.Language']"}),
            'pattern': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'implementations'", 'to': "orm['pattern.Pattern']"})
        },
        'pattern.language': {
            'Meta': {'object_name': 'Language'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'super_lang': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'dialects'", 'null': 'True', 'to': "orm['pattern.Language']"}),
            'wikipedia': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'pattern.pattern': {
            'Meta': {'object_name': 'Pattern'},
            'consequences': ('django.db.models.fields.TextField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'intent': ('django.db.models.fields.TextField', [], {}),
            'motivation': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'structure': ('django.db.models.fields.TextField', [], {}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'patterns'", 'symmetrical': 'False', 'to': "orm['pattern.Tags']"})
        },
        'pattern.tags': {
            'Meta': {'object_name': 'Tags'},
            'icon': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {})
        },
        'pattern.use': {
            'Meta': {'object_name': 'Use'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'line_end': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'line_start': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pattern': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'uses'", 'to': "orm['pattern.Pattern']"}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['pattern']