# -*- coding: utf-8 -*-
from django.test import TestCase
from django.test.client import Client, RequestFactory


class ViewsTestCase(TestCase):
    fixtures = ['books.yaml']

    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()

    def test_should_exists_a_url_for_books(self):
        response = self.client.get('/books')
        self.assertEquals(200, response.status_code)
