from django.db import models
from django.utils import timezone

class ClientMaster(models.Model):
    client_id = models.AutoField(primary_key=True)
    co_name = models.CharField(max_length=255)
    generated = models.IntegerField(default=timezone.now)

    class Meta:
        managed = False
        db_table = "'general'.'client_master'"

class CountryMaster(models.Model):
    country_id = models.AutoField(primary_key=True, db_column='country_id')
    country_name = models.CharField(max_length=255, db_column='country_name')
    generated = models.IntegerField(default=models.functions.Extract(models.F('current_timestamp'), 'epoch'), db_column='generated')

    class Meta:
        managed = False
        db_table = "'general'.'country_master'"

class StateMaster(models.Model):
    state_id = models.AutoField(primary_key=True, db_column='state_id')
    state_name = models.CharField(max_length=255, db_column='state_name')
    country = models.ForeignKey(CountryMaster, on_delete=models.CASCADE, db_column='country_id')
    generated = models.IntegerField(default=models.functions.Extract(models.F('current_timestamp'), 'epoch'), db_column='generated')

    class Meta:
        managed = False
        db_table = "'general'.'state_master'"

class CityMaster(models.Model):
    city_id = models.AutoField(primary_key=True, db_column='city_id')
    city_name = models.CharField(max_length=255, db_column='city_name')
    state = models.ForeignKey(StateMaster, on_delete=models.CASCADE, db_column='state_id')
    generated = models.IntegerField(default=models.functions.Extract(models.F('current_timestamp'), 'epoch'), db_column='generated')

    class Meta:
        managed = False
        db_table = "'general'.'city_master'"

class CompanyMaster(models.Model):
    co_id = models.AutoField(primary_key=True, db_column='co_id')
    client = models.ForeignKey(ClientMaster, on_delete=models.CASCADE, db_column='client_id')
    co_name = models.CharField(max_length=255, db_column='co_name')
    address = models.CharField(max_length=255, db_column='address')
    pincode = models.IntegerField(db_column='pincode')
    city = models.ForeignKey(CityMaster, on_delete=models.CASCADE, db_column='city_id')
    country = models.ForeignKey(CountryMaster, on_delete=models.CASCADE, db_column='country_id')
    state = models.ForeignKey(StateMaster, on_delete=models.CASCADE, db_column='state_id')
    generated = models.IntegerField(default=models.functions.Extract(models.F('current_timestamp'), 'epoch'), db_column='generated')

    class Meta:
        managed = False
        db_table = "'general'.'company_master'"
