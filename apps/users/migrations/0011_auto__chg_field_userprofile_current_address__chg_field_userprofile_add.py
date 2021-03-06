# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'UserProfile.current_address'
        db.alter_column(u'users_userprofile', 'current_address', self.gf('django.contrib.gis.db.models.fields.PointField')(null=True))

        # Changing field 'UserProfile.address_coordinates'
        db.alter_column(u'users_userprofile', 'address_coordinates', self.gf('django.contrib.gis.db.models.fields.PointField')(null=True))

    def backwards(self, orm):

        # Changing field 'UserProfile.current_address'
        db.alter_column(u'users_userprofile', 'current_address', self.gf('jsonfield.fields.JSONField')(max_length=9999))

        # Changing field 'UserProfile.address_coordinates'
        db.alter_column(u'users_userprofile', 'address_coordinates', self.gf('jsonfield.fields.JSONField')(max_length=9999))

    models = {
        u'users.earlybirduser': {
            'Meta': {'object_name': 'EarlyBirdUser'},
            'confirmed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone': ('phonenumber_field.modelfields.PhoneNumberField', [], {'unique': 'True', 'max_length': '16'}),
            'registered_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'})
        },
        u'users.userevents': {
            'Meta': {'object_name': 'UserEvents'},
            'event': ('django.db.models.fields.IntegerField', [], {'default': '1', 'max_length': '2'}),
            'extrainfo': ('jsonfield.fields.JSONField', [], {'default': "'{}'", 'max_length': '9999'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['users.UserProfile']"})
        },
        u'users.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'account_status': ('django.db.models.fields.IntegerField', [], {'default': '1', 'max_length': '1'}),
            'address': ('jsonfield.fields.JSONField', [], {'default': "'{}'", 'max_length': '9999'}),
            'address_coordinates': ('django.contrib.gis.db.models.fields.PointField', [], {'default': "'POINT (85.3141498444705064 27.6942413607694782)'", 'null': 'True', 'blank': 'True'}),
            'current_address': ('django.contrib.gis.db.models.fields.PointField', [], {'default': "'POINT (85.3141498444705064 27.6942413607694782)'", 'null': 'True', 'blank': 'True'}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'extrainfo': ('jsonfield.fields.JSONField', [], {'default': "'{}'", 'max_length': '9999'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'phone': ('phonenumber_field.modelfields.PhoneNumberField', [], {'unique': 'True', 'max_length': '16'}),
            'phone_status': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'profile_image': ('django.db.models.fields.files.ImageField', [], {'default': "''", 'max_length': '1024', 'blank': 'True'}),
            'user_type': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'userref': ('django.db.models.fields.CharField', [], {'default': "'a00f0b8e56ef48b7a10746f28f8b3be4'", 'unique': 'True', 'max_length': '100'})
        },
        u'users.usertoken': {
            'Meta': {'object_name': 'UserToken'},
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'timeframe': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'token': ('django.db.models.fields.CharField', [], {'max_length': '20', 'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['users.UserProfile']"})
        }
    }

    complete_apps = ['users']