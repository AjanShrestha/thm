# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'JobEvents'
        db.create_table(u'jobs_jobevents', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('job', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['jobs.Jobs'])),
            ('event', self.gf('django.db.models.fields.IntegerField')(default=1, max_length=2)),
            ('updated_on', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('extrainfo', self.gf('jsonfield.fields.JSONField')(default='{}', max_length=9999)),
        ))
        db.send_create_signal(u'jobs', ['JobEvents'])

        # Deleting field 'Jobs.tracking_number'
        db.delete_column(u'jobs_jobs', 'tracking_number')

        # Adding field 'Jobs.jobtype'
        db.add_column(u'jobs_jobs', 'jobtype',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


        # Changing field 'Jobs.fee'
        db.alter_column(u'jobs_jobs', 'fee', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=2))

    def backwards(self, orm):
        # Deleting model 'JobEvents'
        db.delete_table(u'jobs_jobevents')

        # Adding field 'Jobs.tracking_number'
        db.add_column(u'jobs_jobs', 'tracking_number',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Deleting field 'Jobs.jobtype'
        db.delete_column(u'jobs_jobs', 'jobtype')


        # Changing field 'Jobs.fee'
        db.alter_column(u'jobs_jobs', 'fee', self.gf('django.db.models.fields.DecimalField')(max_digits=1000, decimal_places=2))

    models = {
        u'jobs.jobevents': {
            'Meta': {'object_name': 'JobEvents'},
            'event': ('django.db.models.fields.IntegerField', [], {'default': '1', 'max_length': '2'}),
            'extrainfo': ('jsonfield.fields.JSONField', [], {'default': "'{}'", 'max_length': '9999'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['jobs.Jobs']"}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'})
        },
        u'jobs.jobs': {
            'Meta': {'object_name': 'Jobs'},
            'available_handymen': ('jsonfield.fields.JSONField', [], {'default': '{}'}),
            'completion_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'considered_handymen': ('django.db.models.fields.TextField', [], {'default': '[]'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['users.UserProfile']"}),
            'distance': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '1000', 'decimal_places': '2'}),
            'fee': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            'handymen': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_complete': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'isaccepted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ishidden': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'isnotified': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'jobtype': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'status': ('django.db.models.fields.TextField', [], {'default': "'New'"})
        },
        u'users.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'account_status': ('django.db.models.fields.IntegerField', [], {'default': '1', 'max_length': '1'}),
            'address': ('jsonfield.fields.JSONField', [], {'default': "'{}'", 'max_length': '9999'}),
            'current_address': ('jsonfield.fields.JSONField', [], {'default': "'{}'", 'max_length': '9999'}),
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
            'user_type': ('django.db.models.fields.IntegerField', [], {'default': '2'})
        }
    }

    complete_apps = ['jobs']