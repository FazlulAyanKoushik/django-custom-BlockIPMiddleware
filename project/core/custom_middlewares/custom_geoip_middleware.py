# geolocation_middleware.py

import requests


class GeolocationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Get the user's IP address from the request
        user_ip = self.get_client_ip(request)

        # Fetch geolocation data based on the IP address
        geolocation_data = self.get_geolocation_data(user_ip)

        # Store the geolocation data in the request
        request.geolocation = geolocation_data

        response = self.get_response(request)
        return response

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def get_geolocation_data(self, ip):
        # Use a geolocation API (e.g., ipinfo.io) to get details based on the IP
        ip = "59.153.103.106"
        url = f"https://ipinfo.io/{ip}/json"
        response = requests.get(url)
        data = response.json()

        # Extract relevant information (e.g., city, country, region)
        geolocation_data = {
            "city": data.get("city"),
            "country": data.get("country"),
            "region": data.get("region"),
            "ip": data.get("ip"),
            "hostname": data.get("hostname"),
            "loc": data.get("loc"),
            "org": data.get("org"),
            "postal": data.get("postal"),
            "timezone": data.get("timezone"),
        }

        return geolocation_data
