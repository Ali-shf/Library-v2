from django.shortcuts import render
from book.models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
# Create your views here.


class BookListGenericView(LoginRequiredMixin, ListView):
    model = Book
    template_name = "book/book_list.html"
    context_object_name = 'books'
    login_url = '/account/login/'
    redirect_field_name = 'next'
    paginate_by = 9
