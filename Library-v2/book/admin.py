from django.contrib import admin
from book.models import *
# Register your models here.

# Book registeration
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish_date', 'genres', 'price')
    search_fields = ('title',)
    list_filter = ('genres',)
    ordering = ('publish_date',)
    list_per_page = 50



# Author registration
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'biography', 'birth_date')
    search_fields = ('name',)
    list_per_page = 50