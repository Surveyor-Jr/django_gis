from django.contrib import admin
from .models import Join, CoordinateTransform, CRS, Polar, FromShapefile

class JoinAdmin(admin.ModelAdmin):
    list_display = ('y_start', 'x_start', 'y_end', 'x_end', 'distance', 'direction_dd')

class PolarAdmin(admin.ModelAdmin):
    list_display = ('x', 'y', 'distance', 'direction', 'x_coordinate', 'y_coordinate')

class CTAdmin(admin.ModelAdmin):
    list_display = ('from_epsg', 'x', 'y', 'to_epsg', 'x_trans', 'y_trans')


admin.site.register(Join, JoinAdmin)
admin.site.register(Polar, PolarAdmin)
admin.site.register(CoordinateTransform, CTAdmin)
admin.site.register(CRS)
admin.site.register(FromShapefile)
