from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Book

class BookAPITesting(APITestCase):
    def test_response_is_correct(self):
        
        book = Book.objects.create(
            title="Demo",
            author="Author",
            isbn="1234567890123",
            published_date="2025-07-26" 
        )
        
        url = reverse('api:book-list') 
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        
        body = response.json()
        returned_book = body[0]
        
        assert returned_book["title"] == book.title
        assert returned_book["author"] == book.author
        assert returned_book["isbn"] == book.isbn
        assert returned_book["published_date"] == str(book.published_date)