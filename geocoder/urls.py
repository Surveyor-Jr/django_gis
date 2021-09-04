from django.urls import path, include
from geocoder import views as geocoder_views

urlpatterns = [
    path('single-address/', geocoder_views.geocode, name='single-address'),
    path('reverse-geocode/', geocoder_views.reverse_geocode, name='reverse-geocode'),
    # path('geocoded-address/', geocoder_views.stored_address, name='my-address'),
    path('batch-geocode/', geocoder_views.batch_geocoding, name='batch-geocode'),
]