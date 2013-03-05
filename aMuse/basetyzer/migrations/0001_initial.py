# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Exhibit'
        db.create_table(u'basetyzer_exhibit', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('date_begin', self.gf('django.db.models.fields.DateField')()),
            ('date_end', self.gf('django.db.models.fields.DateField')()),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal(u'basetyzer', ['Exhibit'])

        # Adding model 'NFC'
        db.create_table(u'basetyzer_nfc', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('serial', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('in_use', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'basetyzer', ['NFC'])

        # Adding model 'Item'
        db.create_table(u'basetyzer_item', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('release_date', self.gf('django.db.models.fields.DateField')()),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('nfc_tag', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['basetyzer.NFC'])),
        ))
        db.send_create_signal(u'basetyzer', ['Item'])

        # Adding M2M table for field exhibit on 'Item'
        db.create_table(u'basetyzer_item_exhibit', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('item', models.ForeignKey(orm[u'basetyzer.item'], null=False)),
            ('exhibit', models.ForeignKey(orm[u'basetyzer.exhibit'], null=False))
        ))
        db.create_unique(u'basetyzer_item_exhibit', ['item_id', 'exhibit_id'])

        # Adding model 'Experience'
        db.create_table(u'basetyzer_experience', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('confirmed', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('hash_url', self.gf('django.db.models.fields.CharField')(max_length=40)),
        ))
        db.send_create_signal(u'basetyzer', ['Experience'])

        # Adding model 'Comment'
        db.create_table(u'basetyzer_comment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'basetyzer', ['Comment'])

        # Adding model 'Photo'
        db.create_table(u'basetyzer_photo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'basetyzer', ['Photo'])

        # Adding model 'Scan'
        db.create_table(u'basetyzer_scan', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['basetyzer.Item'])),
        ))
        db.send_create_signal(u'basetyzer', ['Scan'])

        # Adding model 'Action'
        db.create_table(u'basetyzer_action', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_performed', self.gf('django.db.models.fields.DateTimeField')()),
            ('scan', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['basetyzer.Scan'])),
            ('photo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['basetyzer.Photo'])),
            ('comment', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['basetyzer.Comment'])),
            ('experience', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['basetyzer.Experience'])),
        ))
        db.send_create_signal(u'basetyzer', ['Action'])


    def backwards(self, orm):
        # Deleting model 'Exhibit'
        db.delete_table(u'basetyzer_exhibit')

        # Deleting model 'NFC'
        db.delete_table(u'basetyzer_nfc')

        # Deleting model 'Item'
        db.delete_table(u'basetyzer_item')

        # Removing M2M table for field exhibit on 'Item'
        db.delete_table('basetyzer_item_exhibit')

        # Deleting model 'Experience'
        db.delete_table(u'basetyzer_experience')

        # Deleting model 'Comment'
        db.delete_table(u'basetyzer_comment')

        # Deleting model 'Photo'
        db.delete_table(u'basetyzer_photo')

        # Deleting model 'Scan'
        db.delete_table(u'basetyzer_scan')

        # Deleting model 'Action'
        db.delete_table(u'basetyzer_action')


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
            'comment': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['basetyzer.Comment']"}),
            'date_performed': ('django.db.models.fields.DateTimeField', [], {}),
            'experience': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['basetyzer.Experience']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'photo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['basetyzer.Photo']"}),
            'scan': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['basetyzer.Scan']"})
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
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'hash_url': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'basetyzer.item': {
            'Meta': {'object_name': 'Item'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'exhibit': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['basetyzer.Exhibit']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nfc_tag': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['basetyzer.NFC']"}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'release_date': ('django.db.models.fields.DateField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'basetyzer.nfc': {
            'Meta': {'object_name': 'NFC'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_use': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'serial': ('django.db.models.fields.CharField', [], {'max_length': '50'})
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
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['basetyzer']