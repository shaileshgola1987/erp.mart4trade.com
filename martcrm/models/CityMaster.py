from django.db import models


class CityMaster(models.Model):
    city_id = models.AutoField(primary_key=True)
    city = models.CharField(max_length=100)
    area_code = models.CharField(max_length=50, blank=True, null=True)
    branch = models.CharField(max_length=80, blank=True, null=True)
    country_code = models.ForeignKey('CountryMaster', models.DO_NOTHING, db_column='country_code')
    state = models.CharField(max_length=80)
    population = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    admin = models.CharField(max_length=1, blank=True, null=True)
    latitude = models.CharField(max_length=10, blank=True, null=True)
    longitude = models.CharField(max_length=10, blank=True, null=True)
    time_offset = models.FloatField(blank=True, null=True)
    audit_created_by = models.IntegerField(blank=True, null=True)
    audit_date_created = models.DateTimeField(blank=True, null=True)
    audit_modified_by = models.IntegerField(blank=True, null=True)
    audit_date_modified = models.DateTimeField(blank=True, null=True)
    audit_version = models.IntegerField(blank=True, null=True)
    # audit_id = models.AutoField()
    city_synonym = models.CharField(max_length=100, blank=True, null=True)
    longitude_float = models.FloatField(blank=True, null=True)
    latitude_float = models.FloatField(blank=True, null=True)
    top_city = models.BooleanField(blank=True, null=True)
    search_city = models.BooleanField(default=True)
    seo_city_id = models.IntegerField(blank=True, null=True)
    covid_zone = models.CharField(max_length=50, blank=True, null=True)
    hindi_city = models.CharField(max_length=150, blank=True, null=True)
    city_hi = models.TextField(blank=True, null=True)
    state_hi = models.TextField(blank=True, null=True)
    city_tier = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '"general"."city_master"'