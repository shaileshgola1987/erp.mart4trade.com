from django.db import models
from django.utils import timezone
import time

class ClientMaster(models.Model):
    client_id = models.AutoField(primary_key=True)
    co_name = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=255)
    emailid = models.CharField(max_length=255)
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=15)
    generated = models.IntegerField(default=time.time)

    class Meta:
        managed = False
        db_table = '"general"."client_master"'