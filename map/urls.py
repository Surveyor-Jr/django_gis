from django.urls import path
from map import views as map_views

urlpatterns = [
    path('view-layer/', map_views.map_shapefile, name='view-layer'),
    path('stored-file/', map_views.stored_file, name='stored-file'),
]