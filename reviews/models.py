# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class BooksData(models.Model):
    id = models.CharField(primary_key=True, max_length=40)
    title = models.CharField(max_length=300)
    author = models.CharField(max_length=200)
    year = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)
    publisher = models.ForeignKey('BooksPublisher', models.DO_NOTHING)
    image_url = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'books_data'


class BooksRating(models.Model):
    user = models.ForeignKey('BooksUser', models.CASCADE)
    isbn = models.ForeignKey('BooksData', models.CASCADE)
    rating = models.DecimalField(max_digits=4, decimal_places=0)

    class Meta:
        managed = False
        db_table = 'books_rating'


class BooksUser(models.Model):
    id = models.AutoField(primary_key=True)
    age = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)
    username = models.CharField(unique=True, max_length=40)
    password = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'books_user'


class BooksPublisher(models.Model):
    name = models.CharField(unique=True, max_length=200)

    class Meta:
        managed = False
        db_table = 'books_publisher'
