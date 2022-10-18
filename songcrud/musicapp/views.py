from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, this is my django app")

# Create your views here.
