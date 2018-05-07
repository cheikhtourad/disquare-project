# views.py
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hi there, this is our new home page.")


def hello(request, text):
   x = "Hello "+ text
   return HttpResponse(x)