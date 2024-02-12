from django.db import models


class CountryStates(models.Model):
    state = models.CharField(max_length=80)
    country_code = models.ForeignKey('CountryMaster', models.DO_NOTHING, db_column='country_code', blank=True, null=True, related_name='countrystates_country_code')
    state_abbrev = models.CharField(max_length=10, blank=True, null=True)
    state_id = models.AutoField(primary_key=True)
    zone = models.CharField(max_length=100, blank=True, null=True)
    gst_state_code = models.IntegerField(blank=True, null=True)
    alpha_code = models.CharField(max_length=3, blank=True, null=True)
    state_hi = models.TextField(blank=True, null=True)
    for_gst = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '"general"."country_states"'