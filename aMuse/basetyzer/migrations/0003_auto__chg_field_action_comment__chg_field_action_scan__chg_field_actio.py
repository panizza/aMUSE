# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Action.comment'
        db.alter_column(u'basetyzer_action', 'comment_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['basetyzer.Comment'], null=True))

        # Changing field 'Action.scan'
        db.alter_column(u'basetyzer_action', 'scan_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['basetyzer.Scan'], null=True))

        # Changing field 'Action.photo'
        db.alter_column(u'basetyzer_action', 'photo_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['basetyzer.Photo'], null=True))

    def backwards(self, orm):

        # Changing field 'Action.comment'
        db.alter_column(u'basetyzer_action', 'comment_id', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['basetyzer.Comment']))

        # Changing field 'Action.scan'
        db.alter_column(u'basetyzer_action', 'scan_id', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['basetyzer.Scan']))

        # Changing field 'Action.photo'
        db.alter_column(u'basetyzer_action', 'photo_id', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['basetyzer.Photo']))

    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'basetyzer.action': {
            'Meta': {'object_name': 'Action'},
            'comment': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['basetyzer.Comment']", 'null': 'True'}),
            'date_performed': ('django.db.models.fields.DateTimeField', [], {}),
            'experience': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['basetyzer.Experience']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'photo': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['basetyzer.Photo']", 'null': 'True'}),
            'scan': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['basetyzer.Scan']", 'null': 'True'})
        },
        u'basetyzer.comment': {
            'Meta': {'object_name': 'Comment'},
            'content': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'basetyzer.exhibit': {
            'Meta': {'object_name': 'Exhibit'},
            'date_begin': ('django.db.models.fields.DateField', [], {}),
            'date_end': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'basetyzer.experience': {
            'Meta': {'object_name': 'Experience'},
            'confirmed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'hash_url': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '40'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'basetyzer.item': {
            'Meta': {'object_name': 'Item'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'exhibit': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['basetyzer.Exhibit']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'release_date': ('django.db.models.fields.DateField', [], {}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['basetyzer.Tag']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'basetyzer.photo': {
            'Meta': {'object_name': 'Photo'},
            'content': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'basetyzer.scan': {
            'Meta': {'object_name': 'Scan'},
            'content': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['basetyzer.Item']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'basetyzer.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_use': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'serial': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['basetyzer']