from django.urls import path
from book.views import *

urlpatterns = [
    path('books', BookListGenericView.as_view(), name='book_list'),
]