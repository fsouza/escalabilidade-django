import cProfile

from django.test.client import RequestFactory

from books.views import list_books

factory = RequestFactory()

request = factory.get('/books')
profile = cProfile.Profile()
profile.runcall(list_books, request)
profile.print_stats()
