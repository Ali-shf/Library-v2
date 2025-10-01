from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=255)
    biography = models.TextField()
    birth_date = models.DateField(blank=False)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Book(models.Model):
    GENRES_CHOISES = [
        ('FIN', 'Fiction'),
        ('HIS', 'History'),
        ('SCI', 'Science'),
        ('FANT', 'Fantasy'),
    ]
    title = models.CharField(max_length=255)
    description = models.TextField(null=True)
    publish_date = models.DateField()
    genres = models.CharField(choices=GENRES_CHOISES, max_length=10)
    price = models.BigIntegerField()
    authors = models.ManyToManyField(to=Author, related_name='Book')

    def __str__(self):
        return self.title
    
    def __repr__(self):
        return self.title
    
    

