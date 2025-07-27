from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import BookSerializer
from .models import Book


class BookListView(APIView):
    # GET a list of all books from the server
    def get(self, request, **kwargs):
        all_books = Book.objects.all()
        serializer = BookSerializer(all_books, many=True)
        return Response(serializer.data)
    
    # POST create a new book in the database
    def post(self, request, **kwargs):
        serializer = BookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class BookIndividualView(APIView):

    # GET a book from a list
    def get(self, request, isbn, **kwargs):
        book = Book.objects.get(isbn=isbn)
        serializer = BookSerializer(book)
        return Response(serializer.data)

    # UPDATE a book
    def patch(self, request, isbn, **kwargs):
        book = Book.objects.get(isbn=isbn)
        serializer = BookSerializer(book, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    # DELETE a book
    def delete(self, request, isbn, **kwargs):
        book = Book.objects.get(isbn=isbn)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)