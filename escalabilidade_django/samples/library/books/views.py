# Create your views here.
from django.http import HttpResponse

def list_books(request):
    return HttpResponse("Ok")
