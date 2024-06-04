from django.urls import path

from .views import my_ip_geolocation_data

urlpatterns = [
    path("", my_ip_geolocation_data, name="my_ip_geolocation_data"),
]