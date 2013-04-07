# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'CustomUser'
        db.delete_table(u'basetyzer_customuser')

        # Removing M2M table for field groups on 'CustomUser'
        db.delete_table('basetyzer_customuser_groups')

        # Removing M2M table for field user_permissions on 'CustomUser'
        db.delete_table('basetyzer_customuser_user_permissions')


        # Changing field 'Exhibit.owner'
        db.alter_column(u'basetyzer_exhibit', 'owner_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User']))
        # Deleting field 'Experience.confirmed'
        db.delete_column(u'basetyzer_experience', 'confirmed')

        # Adding field 'Experience.public'
        db.add_column(u'basetyzer_experience', 'public',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


        # Changing field 'Experience.user'
        db.alter_column(u'basetyzer_experience', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User']))

    def backwards(self, orm):
        # Adding model 'CustomUser'
        db.create_table(u'basetyzer_customuser', (
            ('username', self.gf('django.db.models.fields.CharField')(max_length=30, unique=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('need_reset', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_staff', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=128)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_joined', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('is_superuser', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('last_login', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
        ))
        db.send_create_signal(u'basetyzer', ['CustomUser'])

        # Adding M2M table for field groups on 'CustomUser'
        db.create_table(u'basetyzer_customuser_groups', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('customuser', models.ForeignKey(orm[u'basetyzer.customuser'], null=False)),
            ('group', models.ForeignKey(orm[u'auth.group'], null=False))
        ))
        db.create_unique(u'basetyzer_customuser_groups', ['customuser_id', 'group_id'])

        # Adding M2M table for field user_permissions on 'CustomUser'
        db.create_table(u'basetyzer_customuser_user_permissions', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('customuser', models.ForeignKey(orm[u'basetyzer.customuser'], null=False)),
            ('permission', models.ForeignKey(orm[u'auth.permission'], null=False))
        ))
        db.create_unique(u'basetyzer_customuser_user_permissions', ['customuser_id', 'permission_id'])


        # Changing field 'Exhibit.owner'
        db.alter_column(u'basetyzer_exhibit', 'owner_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['basetyzer.CustomUser']))
        # Adding field 'Experience.confirmed'
        db.add_column(u'basetyzer_experience', 'confirmed',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Deleting field 'Experience.public'
        db.delete_column(u'basetyzer_experience', 'public')


        # Changing field 'Experience.user'
        db.alter_column(u'basetyzer_experience', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['basetyzer.CustomUser']))

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
            'Meta': {'ordering': "['experience', 'date_performed']", 'object_name': 'Action'},
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
            'Meta': {'ordering': "['date_begin']", 'object_name': 'Exhibit'},
            'date_begin': ('django.db.models.fields.DateField', [], {}),
            'date_end': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'basetyzer.experience': {
            'Meta': {'ordering': "['date']", 'object_name': 'Experience'},
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'hash_url': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '40'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'basetyzer.item': {
            'Meta': {'ordering': "['pk']", 'object_name': 'Item'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'exhibit': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['basetyzer.Exhibit']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'photo': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'release_date': ('django.db.models.fields.DateField', [], {}),
            'tag': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
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
        u'basetyzer.superqrcode': {
            'Meta': {'object_name': 'SuperQRCode'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_edit': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '40'})
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