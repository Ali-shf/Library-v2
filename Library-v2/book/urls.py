from django.urls import path
from book.views import *

urlpatterns = [
    path('book_list', book_list, name='book_list')
]