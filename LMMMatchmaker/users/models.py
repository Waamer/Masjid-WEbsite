from django.db import models

# Create your models here.
class PersonalData(models.Model):
    age = models.IntegerField()
    body_type = models.CharField(max_length=50)
    weight = models.IntegerField()
    height = models.IntegerField()
    is_muslim = models.CharField(max_length=3, null=True, blank=True)
    muslim_type = models.CharField(max_length=10, null=True, blank=True)
    is_converted = models.CharField(max_length=7, null=True, blank=True)
    convert_time = models.CharField(max_length=20)
    prayers = models.CharField(max_length=30)
    masjid = models.CharField(max_length=40)
