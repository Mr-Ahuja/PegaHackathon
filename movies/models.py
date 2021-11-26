from django.db import models
from datetime import date

class Movie(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    year = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey('auth.User', related_name='movies', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-id']


class Vaccines(models.Model):
    vid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    disease = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

class VaccinesRegistered(models.Model):
    username = models.CharField(max_length=100)
    doseNumber = models.IntegerField()
    vid = models.ForeignKey(Vaccines, on_delete=models.CASCADE)
    dose_date = models.DateField(("Date"), default=date.today)
    provider_name = models.CharField(max_length=100)

class BookingDetails(models.Model):
    bid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    vid = models.ForeignKey(Vaccines, on_delete=models.CASCADE)
    status = models.BooleanField()

class HealthProvider(models.Model):
    did = models.AutoField(primary_key=True)
    providerName = models.CharField(max_length=100)
    totalDose = models.IntegerField()
    driveDate = models.DateField(("Date"), default=date.today)