from django.urls import path, include
from chatbot import views as chatbot_views

urlpatterns = [
    path('chatbot/', chatbot_views.api_request, name='api-request'),
]