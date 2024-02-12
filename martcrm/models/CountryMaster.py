from django.db import models

class CountryMaster(models.Model):
    country_code = models.CharField(primary_key=True, max_length=10)
    name = models.CharField(max_length=100)
    risk_level = models.CharField(max_length=20)
    isd_code = models.IntegerField(blank=True, null=True)
    cr_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    cr_price_old = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    continent = models.CharField(max_length=50, blank=True, null=True)
    record_type = models.CharField(max_length=30)
    im_contact = models.BooleanField(blank=True, null=True)
    sms_allowed = models.BooleanField(blank=True, null=True)
    neighbour_countries = models.TextField(blank=True, null=True)  # This field type is a guess.
    name_hi = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '"general"."country_master"'