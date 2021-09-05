from django.urls import path, include
from users import views as user_views
from .views import GeocodeList

urlpatterns = [    
    path('', user_views.home, name='profile-home'),
    path('single-address-geocodes/', GeocodeList.as_view(), name='single-address-geocode-list')
]