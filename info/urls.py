from django.urls import path, include
from info import views as info_views
urlpatterns = [    
    path('', info_views.LandingPage, name='home'),
]