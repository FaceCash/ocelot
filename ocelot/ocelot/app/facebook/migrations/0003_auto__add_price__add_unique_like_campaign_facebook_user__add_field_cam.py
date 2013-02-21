# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Price'
        db.create_table('facebook_price', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True, db_index=True)),
            ('total', self.gf('django.db.models.fields.DecimalField')(default=0.0, max_digits=7, decimal_places=2)),
            ('user_commission', self.gf('django.db.models.fields.DecimalField')(default=0.0, max_digits=7, decimal_places=2)),
        ))
        db.send_create_signal('facebook', ['Price'])

        # Adding unique constraint on 'Like', fields ['campaign', 'facebook_user']
        db.create_unique('facebook_like', ['campaign_id', 'facebook_user_id'])

        # Adding field 'Campaign.title'
        db.add_column('facebook_campaign', 'title',
                      self.gf('django.db.models.fields.CharField')(default='Title', max_length=300),
                      keep_default=False)

        # Adding field 'Campaign.owner'
        db.add_column('facebook_campaign', 'owner',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name=u'owner', to=orm['fandjango.User']),
                      keep_default=False)

        # Adding field 'Campaign.price'
        db.add_column('facebook_campaign', 'price',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['facebook.Price']),
                      keep_default=False)

        # Adding field 'Campaign.limit_likes'
        db.add_column('facebook_campaign', 'limit_likes',
                      self.gf('django.db.models.fields.IntegerField')(default=100),
                      keep_default=False)


    def backwards(self, orm):
        # Removing unique constraint on 'Like', fields ['campaign', 'facebook_user']
        db.delete_unique('facebook_like', ['campaign_id', 'facebook_user_id'])

        # Deleting model 'Price'
        db.delete_table('facebook_price')

        # Deleting field 'Campaign.title'
        db.delete_column('facebook_campaign', 'title')

        # Deleting field 'Campaign.owner'
        db.delete_column('facebook_campaign', 'owner_id')

        # Deleting field 'Campaign.price'
        db.delete_column('facebook_campaign', 'price_id')

        # Deleting field 'Campaign.limit_likes'
        db.delete_column('facebook_campaign', 'limit_likes')


    models = {
        'facebook.campaign': {
            'Meta': {'object_name': 'Campaign'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'facebook_id': ('django.db.models.fields.BigIntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'likers': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'Campaigns'", 'symmetrical': 'False', 'through': "orm['facebook.Like']", 'to': "orm['fandjango.User']"}),
            'limit_likes': ('django.db.models.fields.IntegerField', [], {'default': '100'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'owner'", 'to': "orm['fandjango.User']"}),
            'price': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['facebook.Price']"}),
            'title': ('django.db.models.fields.CharField', [], {'default': "'Title'", 'max_length': '300'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'facebook.like': {
            'Meta': {'unique_together': "(('campaign', 'facebook_user'),)", 'object_name': 'Like'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'campaign': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'likes'", 'to': "orm['facebook.Campaign']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'facebook_user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'likes'", 'to': "orm['fandjango.User']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'facebook.price': {
            'Meta': {'object_name': 'Price'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'total': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '7', 'decimal_places': '2'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user_commission': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '7', 'decimal_places': '2'})
        },
        'fandjango.oauthtoken': {
            'Meta': {'object_name': 'OAuthToken'},
            'expires_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issued_at': ('django.db.models.fields.DateTimeField', [], {}),
            'token': ('django.db.models.fields.TextField', [], {})
        },
        'fandjango.user': {
            'Meta': {'object_name': 'User'},
            'authorized': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'birthday': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'facebook_id': ('django.db.models.fields.BigIntegerField', [], {'unique': 'True'}),
            'facebook_username': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'last_seen_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'middle_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'oauth_token': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['fandjango.OAuthToken']", 'unique': 'True'})
        }
    }

    complete_apps = ['facebook']