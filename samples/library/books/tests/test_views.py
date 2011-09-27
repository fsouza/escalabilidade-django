# -*- coding: utf-8 -*-
from django.test import TestCase
from django.test.client import Client, RequestFactory

from books.views import list_books


class ViewsTestCase(TestCase):
    fixtures = ['books.yaml']

    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()

    def test_should_exists_a_url_for_books(self):
        response = self.client.get('/books')
        self.assertEquals(200, response.status_code)

    def test_should_return_the_books_list_in_the_context(self):
        request = self.factory.get('/books')
        response = list_books(request)
        books_list = response.context_data['books']

        self.assertEquals(23, len(books_list))
