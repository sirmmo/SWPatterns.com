# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Pattern'
        db.create_table('pattern_pattern', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.TextField')()),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('intent', self.gf('django.db.models.fields.TextField')()),
            ('motivation', self.gf('django.db.models.fields.TextField')()),
            ('structure', self.gf('django.db.models.fields.TextField')()),
            ('consequences', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('pattern', ['Pattern'])

        # Adding M2M table for field tags on 'Pattern'
        db.create_table('pattern_pattern_tags', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('pattern', models.ForeignKey(orm['pattern.pattern'], null=False)),
            ('tags', models.ForeignKey(orm['pattern.tags'], null=False))
        ))
        db.create_unique('pattern_pattern_tags', ['pattern_id', 'tags_id'])

        # Adding model 'Tags'
        db.create_table('pattern_tags', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('pattern', ['Tags'])

        # Adding model 'Language'
        db.create_table('pattern_language', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.TextField')()),
            ('wikipedia', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('super_lang', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='dialects', null=True, to=orm['pattern.Language'])),
        ))
        db.send_create_signal('pattern', ['Language'])

        # Adding model 'Implementation'
        db.create_table('pattern_implementation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pattern', self.gf('django.db.models.fields.related.ForeignKey')(related_name='implementations', to=orm['pattern.Pattern'])),
            ('gist', self.gf('django.db.models.fields.IntegerField')()),
            ('language', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pattern.Language'])),
        ))
        db.send_create_signal('pattern', ['Implementation'])

        # Adding model 'Use'
        db.create_table('pattern_use', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pattern', self.gf('django.db.models.fields.related.ForeignKey')(related_name='uses', to=orm['pattern.Pattern'])),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('line_start', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('line_end', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('pattern', ['Use'])

    def backwards(self, orm):
        # Deleting model 'Pattern'
        db.delete_table('pattern_pattern')

        # Removing M2M table for field tags on 'Pattern'
        db.delete_table('pattern_pattern_tags')

        # Deleting model 'Tags'
        db.delete_table('pattern_tags')

        # Deleting model 'Language'
        db.delete_table('pattern_language')

        # Deleting model 'Implementation'
        db.delete_table('pattern_implementation')

        # Deleting model 'Use'
        db.delete_table('pattern_use')

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