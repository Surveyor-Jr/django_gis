from django.db import models
from pyproj import CRS, Transformer

class Join(models.Model):
    start_name = models.CharField(max_length=200, null=True, blank=True)
    y_start = models.FloatField()
    x_start = models.FloatField()
    end_name = models.CharField(max_length=200, null=True, blank=True)
    y_end = models.FloatField()
    x_end = models.FloatField()
    # Results of the Calculation to be stored
    distance = models.FloatField(null=True, blank=True)
    direction_dd = models.FloatField(null=True, blank=True)
    direction_deg = models.IntegerField(null=True, blank=True)
    direction_min = models.IntegerField(null=True, blank=True)
    direction_sec = models.FloatField(null=True, blank=True)
    # Store the date and time information too
    stored_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Calculated Joins'

    def __str__(self):
        return str(self.stored_on)

class Polar(models.Model):
    station_name = models.CharField(max_length=200, null=True, blank=True)
    x = models.FloatField()
    y = models.FloatField()
    distance = models.FloatField()
    direction = models.CharField(max_length=200)
    end_name = models.CharField(max_length=200, null=True, blank=True)
    # Results of the calculation
    x_coordinate = models.FloatField(null=True, blank=True)
    y_coordinate = models.FloatField(null=True, blank=True)
    # Store the date and time information too
    stored_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Calculated Polars'

    def __str__(self):
        return str(self.stored_on) 


class CRS(models.Model):
    name = models.CharField(max_length=200, unique=True, primary_key=True)
    details = models.TextField()
    # UTM_Zone = models.CharField(max_length=200)
    # TODO: To add more attributes {Unit, Area, Accuracy based on https://epsg.io/}

    class Meta:
        verbose_name_plural = 'Coordinate Reference Systems'

    def __str__(self):
        return self.name 

class CoordinateTransform(models.Model):
    from_epsg = models.ForeignKey(CRS, on_delete=models.CASCADE, related_name='from_epsg')
    x = models.FloatField(verbose_name="X/Lon")
    y = models.FloatField(verbose_name="Y/Lat")
    to_epsg = models.ForeignKey(CRS, on_delete=models.CASCADE, related_name='to_epsg')
    x_trans = models.FloatField(verbose_name='X-Transformed', null=True, blank=True)
    y_trans = models.FloatField(verbose_name='Y-Transformed', null=True, blank=True)
    stored_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Coordinate Conversions'       


    def __str__(self):
        return str(self.stored_on)




