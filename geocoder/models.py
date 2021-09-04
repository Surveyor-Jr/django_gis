from django.db import models

# Create your models here.
class SingleAddressGeocode(models.Model):
    address = models.CharField(max_length=200, null=True)
    date = models.DateTimeField(auto_now_add=True)
    lat = models.FloatField(null=True, blank=True)
    lon = models.FloatField(null=True, blank=True)
    full_address = models.TextField(null=True, blank=True)
    metadata = models.JSONField(null=True, blank=True)
    html_map = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.address

    class Meta:
        verbose_name_plural = 'Single Address Geocodes'


class ReverseGeocode(models.Model):
    lat = models.FloatField()
    lon = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    full_address = models.TextField(null=True, blank=True)
    metadata = models.JSONField(null=True, blank=True)
    html_map = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.full_address

    class Meta:
        verbose_name_plural = 'Reverse Geocoded coordinates'

