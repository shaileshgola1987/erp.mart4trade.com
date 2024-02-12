# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AccountEmails(models.Model):
    uniq_id = models.AutoField(primary_key=True)
    userid = models.ForeignKey('UserAccounts', models.DO_NOTHING, db_column='userid', related_name='accountemails_userid')
    email_key = models.ForeignKey('EmailMaster', models.DO_NOTHING, db_column='email_key', related_name='accountemails_email_key')
    ifdefault = models.BooleanField(null=True)

    class Meta:
        managed = False
        db_table = '"general"."account_emails"'
        unique_together = (('userid', 'email_key'),)
