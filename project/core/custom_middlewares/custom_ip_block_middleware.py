"""Custom IP Block Middleware"""

from django.http import HttpResponseForbidden


class CustomIPBlockMiddleware:
    """Custom IP Block Middleware"""

    def __init__(self, get_response):
        self.get_response = get_response
        self.ip_block_list = []

    def __call__(self, request):
        ip = request.META.get('REMOTE_ADDR')
        if ip in self.ip_block_list:
            return HttpResponseForbidden()
        response = self.get_response(request)
        return response
