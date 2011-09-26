# -*- coding: utf-8 -*-
from django.utils import unittest

from books.models import Book

extract_field_names = lambda model: [field.name for field in model._meta.fields]

class BookTestCase(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.names = extract_field_names(Book)

    def test_model_book_should_have_a_title(self):
        self.assertIn('title', self.names)

    def test_model_book_should_have_an_author(self):
        self.assertIn('author', self.names)
