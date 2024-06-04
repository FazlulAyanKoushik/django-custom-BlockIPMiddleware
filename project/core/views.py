from django.shortcuts import render
from django.http import HttpResponse as HTTPResponse


# Create your views here.
def my_ip_geolocation_data(request):
    # Access the geolocation data from the request object
    geolocation_data = request.geolocation

    # Render the template with the geolocation data
    return HTTPResponse(
        f"Data: {geolocation_data}")
