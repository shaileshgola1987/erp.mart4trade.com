# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AccountProfiles(models.Model):
    id = models.AutoField(primary_key=True,db_column='uniq_id')
    userid = models.ForeignKey('UserAccounts', models.DO_NOTHING, db_column='userid', related_name='accountprofiles_userid')
    profile = models.ForeignKey('ProfileMaster', models.DO_NOTHING, blank=True, null=True, related_name='accountprofiles_profile')
    default_account = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = '"general"."account_profiles"'
        unique_together = (('userid', 'profile'),)
