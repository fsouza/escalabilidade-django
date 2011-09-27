# Create your views here.
from django.template.response import TemplateResponse

from books.models import Book


def list_books(request):
    books = Book.objects.all()
    return TemplateResponse(request, "books_list.html", locals())
