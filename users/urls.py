from django.urls import path, include
from .views import GeocodeList, JoinList, PolarList
from users import views as user_views

urlpatterns = [   
    # App Views
    path('', user_views.home, name='profile-home'),
    path('single-address-geocodes/', GeocodeList.as_view(), name='single-address-geocode-list'),
    path('join-results/', JoinList.as_view(), name='calculated-joins'),
    path('polar-results/', PolarList.as_view(), name='calculated-polars'),
]