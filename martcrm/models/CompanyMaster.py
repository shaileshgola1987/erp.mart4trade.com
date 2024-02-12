from django.db import models


class CompanyMaster(models.Model):
    co_id = models.AutoField(primary_key=True)
    client_id = models.IntegerField(blank=True, null=True)
    co_name = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    pincode = models.IntegerField(blank=True, null=True)
    city = models.ForeignKey('CityMaster', models.DO_NOTHING, blank=True, null=True)
    country = models.ForeignKey('CountryMaster', models.DO_NOTHING, blank=True, null=True)
    state = models.ForeignKey('StateMaster', models.DO_NOTHING, blank=True, null=True)
    generated = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '"general"."company_master"'
