# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class WebCategoryMaster(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=180)
    type = models.CharField(max_length=20)
    eypprint_category_id = models.IntegerField(blank=True, null=True)
    iidprint_category_id = models.IntegerField(blank=True, null=True)
    ipprint_category_id = models.IntegerField(blank=True, null=True)
    keywords_vec = models.TextField(blank=True, null=True)  # This field type is a guess.
    keywords = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)
    catalog_gallery = models.IntegerField(blank=True, null=True)
    data_count = models.IntegerField(blank=True, null=True)
    multilingual_catalogs = models.IntegerField(default=0)
    audit_created_by = models.IntegerField(blank=True, null=True)
    audit_date_created = models.DateTimeField(blank=True, null=True)
    audit_modified_by = models.IntegerField(blank=True, null=True)
    audit_date_modified = models.DateTimeField(blank=True, null=True)
    audit_version = models.IntegerField(blank=True, null=True)
    parrent_id = models.IntegerField(blank=True, null=True)
    has_content = models.BooleanField(default=False)
    pref_exp = models.BooleanField(default=False)
    pref_manu = models.BooleanField(default=False)
    pref_imp = models.BooleanField(default=False)
    risk_category = models.CharField(max_length=30, blank=True, null=True)
    ind_chem_prod_cnt = models.IntegerField(blank=True, null=True)
    b2c = models.BooleanField(blank=True, null=True)
    upper_cat_url = models.CharField(max_length=255, blank=True, null=True)
    sale_status = models.CharField(max_length=15)
    gd_dist = models.BooleanField(blank=True, null=True)
    gd_fran = models.BooleanField(blank=True, null=True)
    gd_sales = models.BooleanField(blank=True, null=True)
    exclusive_for_gd = models.BooleanField(blank=True, null=True)
    list_view_type = models.CharField(max_length=15, blank=True, null=True)
    es_products_count = models.IntegerField(blank=True, null=True)
    es_company_count = models.IntegerField(blank=True, null=True)
    rel_micro = models.BooleanField(blank=True, null=True)
    name_hi = models.TextField(blank=True, null=True)
    name_ml = models.TextField(blank=True, null=True)
    name_bn = models.TextField(blank=True, null=True)
    name_ta = models.TextField(blank=True, null=True)
    name_gu = models.TextField(blank=True, null=True)
    name_te = models.TextField(blank=True, null=True)
    name_kn = models.TextField(blank=True, null=True)
    name_mr = models.TextField(blank=True, null=True)
    name_ar = models.TextField(blank=True, null=True)
    name_uz = models.TextField(blank=True, null=True)
    name_vi = models.TextField(blank=True, null=True)
    name_fr = models.TextField(blank=True, null=True)
    name_de = models.TextField(blank=True, null=True)
    name_es = models.TextField(blank=True, null=True)
    name_it = models.TextField(blank=True, null=True)
    name_ja = models.TextField(blank=True, null=True)
    name_ko = models.TextField(blank=True, null=True)
    name_ru = models.TextField(blank=True, null=True)
    name_pt = models.TextField(blank=True, null=True)
    name_zh = models.TextField(blank=True, null=True)
    name_nl = models.TextField(blank=True, null=True)
    disclaimer_message = models.TextField(blank=True, null=True)
    category_description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '"general"."web_category_master"'
