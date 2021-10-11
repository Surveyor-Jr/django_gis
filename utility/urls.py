from django.urls import path, include
from utility import views as utility_views
from .views import ConversionHome

urlpatterns = [    
    path('distance/', utility_views.geodesic_distance, name='distance'),
    path('join/', utility_views.join, name='join'),
    path('polar/', utility_views.polar, name='polar'),
    path('coordinate-transformation/', utility_views.coordinate_transform, name='coordinate-transform'), 
    path('conversion/', ConversionHome.as_view(), name='conversion-home'),
    path('from-shapefile/', utility_views.fromShapefile, name='from-shapefile')
]