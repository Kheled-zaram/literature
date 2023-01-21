from django.shortcuts import render, get_object_or_404
from .filters import ReviewsFilter
from .models import BooksData, BooksPublisher
from django.db.models import Q
from django.views.generic import ListView, DetailView

def home(request):
    # df = query('select * from books_users limit 1000')
    publishers = BooksPublisher.objects.all().values('name')
    search_query = request.GET.get('search', '')
    if is_query_valid(search_query):
        books = BooksData.objects.filter(Q(title__icontains=search_query) | Q(author__icontains=search_query))
        print("searched sth\n")
    else:
        books = BooksData.objects.all()

    min_rating = request.GET.get('min_rating', '')
    max_rating = request.GET.get('max_rating', '')
    min_year = request.GET.get('min_year', '')
    max_year = request.GET.get('max_year', '')
    publisher = request.GET.get('publisher', '')

    if is_query_valid(min_year):
        books = books.filter(year__gte=min_year)
        print("filtered sth: " + min_year)
    if is_query_valid(max_year):
        books = books.filter(year__lte=max_year)
        print("filtered sth: " + max_year)
    if is_query_valid(publisher) and publisher != 'Choose...':
        books = books.filter(publisher__exact=get_object_or_404(BooksPublisher, name=publisher))

    context = {
        'books': books,
        'publishers': publishers
    }
    return render(request, 'reviews/home.html', context)


def about(request):
    return render(request, 'reviews/about.html', {'title': 'About'})


def search(request):
    return render(request, 'reviews/home.html')

def is_query_valid(param):
    return param is not None and param != ''