from django.http import HttpResponse


class CustomExceptionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if response.status_code == 500:
            return response
        return response

    def process_exception(self, request, exception):
        return HttpResponse("Internal Server Error", status=500)
