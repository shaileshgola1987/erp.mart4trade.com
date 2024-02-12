# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class UserAccounts(models.Model):
    userid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50, blank=True, null=True)
    title = models.CharField(max_length=15, blank=True, null=True)
    fname = models.CharField(max_length=200, blank=True, null=True)
    mname = models.CharField(max_length=30, blank=True, null=True)
    lname = models.CharField(max_length=30, blank=True, null=True)
    desg = models.CharField(max_length=100, blank=True, null=True)
    creation_date = models.IntegerField(blank=True, null=True)
    creation_time = models.IntegerField(blank=True, null=True)
    last_visit = models.IntegerField(blank=True, null=True)
    activation_code = models.FloatField(blank=True, null=True)
    auto_registered = models.BooleanField()
    buy_inquiry = models.BooleanField()
    sell_inquiry = models.BooleanField()
    webmail_status = models.CharField(max_length=20)
    account_status = models.CharField(max_length=20)
    section_id = models.IntegerField(blank=True, null=True)
    heard_from = models.IntegerField(blank=True, null=True)
    sms_balance = models.IntegerField(blank=True, null=True)
    last_visit_time = models.IntegerField(blank=True, null=True)
    id_verified = models.BooleanField()
    unmoderated_inq = models.BooleanField()
    tradealert_del_pref = models.CharField(max_length=10, blank=True, null=True)
    terms_accepted = models.BooleanField(blank=True, null=True)
    inq_orig_pref = models.IntegerField(blank=True, null=True)
    generated_e = models.IntegerField(blank=True, null=True)
    roaming_access = models.BooleanField(blank=True, null=True)
    last_password_change = models.IntegerField(blank=True, null=True)
    buy_rfis_limit = models.IntegerField(blank=True, null=True)
    pw_hash = models.TextField()
    password_uncr = models.CharField(max_length=15, blank=True, null=True)
    rfis_rate = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    avg_rfis_resp_time = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    show_rfis_rate = models.BooleanField(blank=True, null=True)
    buyer_feedback = models.IntegerField(blank=True, null=True)
    show_buyer_feedback = models.BooleanField(blank=True, null=True)
    hide_rfis_rate = models.BooleanField(blank=True, null=True)
    hide_buyer_feedback = models.BooleanField(blank=True, null=True)
    inq_to_all_users = models.BooleanField(blank=True, null=True)
    mark_inquiry_cc = models.BooleanField(blank=True, null=True)
    user_image = models.TextField(blank=True, null=True)
    miss_call_alert = models.BooleanField(blank=True, null=True)
    merchant_account_id = models.TextField(blank=True, null=True)
    google_tnc_accepted = models.BooleanField(blank=True, null=True)
    google_ads_account_id = models.BigIntegerField(blank=True, null=True)
    is_gmc_link_with_ads = models.BooleanField(blank=True, null=True)
    adhaar_no = models.CharField(max_length=100, blank=True, null=True)
    username_hi = models.TextField(blank=True, null=True)
    desg_hi = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '"general"."user_accounts"'
