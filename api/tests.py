from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Book

class BookAPITesting(APITestCase):
    # Set up test enviroment witha generic book
    def setUp(self):
        self.book = Book.objects.create(
            title="Dune",
            author="Frank Herbert",
            isbn="9780441013593",
            published_date="1965-08-01"
        )
        self.book_isbn = self.book.isbn
        self.list_create_url = reverse('api:book-list')
        self.detail_url = reverse('api:book-detail', kwargs={'isbn': self.book_isbn})

    # Tests that the API returns the book created in setUp
    def test_response_is_correct(self):
        response = self.client.get(self.list_create_url, format='json')
        assert response.status_code == status.HTTP_200_OK
        body = response.json()
        assert len(body) == 1  
        returned_book = body[0]
        # Check if the returned book matches the setUp book
        assert returned_book["title"] == self.book.title
        assert returned_book["author"] == self.book.author
        assert returned_book["isbn"] == self.book.isbn
        assert returned_book["published_date"] == str(self.book.published_date)

    # Tests that a new book can be created via the API
    def test_create_book(self):
        data = {
            'title': 'Foundation',
            'author': 'Isaac Asimov',
            'isbn': '9780553803716',
            'published_date': '1951-06-01'
        }
        response = self.client.post(self.list_create_url, data, format='json')
        assert response.status_code == status.HTTP_201_CREATED
        # Check iff there are only 2 books
        assert Book.objects.count() == 2

    # Tests if we can retrive book by ISBN
    def test_retrieve_book(self):
        response = self.client.get(self.detail_url, format='json')
        assert response.status_code == status.HTTP_200_OK
        body = response.json()
        assert body['title'] == 'Dune'

    # Tests if we can edit a book entry
    def test_update_book(self):
        data = {'title': 'Dune (Updated)'}
        response = self.client.patch(self.detail_url, data, format='json')
        assert response.status_code == status.HTTP_200_OK
        self.book.refresh_from_db()
        assert self.book.title == 'Dune (Updated)'

    # Test if we can delete a book
    def test_delete_book(self):
        response = self.client.delete(self.detail_url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert Book.objects.count() == 0
