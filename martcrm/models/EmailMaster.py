# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class EmailMaster(models.Model):
    email_key = models.AutoField(primary_key=True)
    email = models.CharField(max_length=250)
    mail_pref = models.CharField(max_length=4)
    verification_status = models.CharField(max_length=20)
    last_sent = models.IntegerField(blank=True, null=True)
    verified = models.BooleanField(blank=True, null=True)
    last_verified_on = models.IntegerField(blank=True, null=True)
    checked_by = models.CharField(max_length=10, blank=True, null=True)
    last_verified_by = models.IntegerField(blank=True, null=True)
    verification_source = models.CharField(max_length=20, blank=True, null=True)
    last_logged_in = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '"general"."email_master"'
