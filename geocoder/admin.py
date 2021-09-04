from django.contrib import admin
from .models import SingleAddressGeocode, ReverseGeocode

class SAGAdmin(admin.ModelAdmin):
    list_display = ('address', 'lat', 'lon', 'full_address')


class RGAdmin(admin.ModelAdmin):
    list_display = ('lat', 'lon', 'latitude', 'longitude', 'full_address')

# Register your models here.
admin.site.register(SingleAddressGeocode, SAGAdmin)
admin.site.register(ReverseGeocode ,RGAdmin)
