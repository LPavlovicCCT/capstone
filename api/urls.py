from django.urls import re_path
from .views import BookListView, BookIndividualView

app_name = 'api'

urlpatterns = [

    # GET and POST go to api/books/
    # No ISBN GET gets a list of all books
    re_path(
        r"^books/$", BookListView.as_view(), name='book-list'
    ),
    
    # GET PATCH and DELETE go to api/books/<ISBN>/
    re_path(
        r"^books/(?P<isbn>\w+)/$", BookIndividualView.as_view(), name='book-detail'
    ),

]