from datetime import datetime

from django.shortcuts import render, get_object_or_404, redirect
from .models import BooksData, BooksPublisher, BooksRating, BooksSession, BooksUser
from django.db.models import Q, Avg, Count, ExpressionWrapper, Subquery, Max, OuterRef
import pandas as pd
from django.db import connection

asc = 'Ascending'
desc = 'Descending'
sorting_options = {'Title', 'Author', 'Year', 'Rating', 'Popularity'}
order_types = {asc, desc}

sort_map = {
    'Title': 'title',
    'Author': 'author',
    'Year': 'year',
    'Rating': 'average_rating',
    'Popularity': 'count_rating'
}


def home(request):
    session_exists = request.session.exists(request.session.session_key)
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

    books = books.annotate(average_rating=Avg('booksrating__rating'))
    books = books.annotate(count_rating=Count('booksrating__rating'))

    if is_query_valid(min_rating):
        books = books.filter(average_rating__gte=min_rating)
    if is_query_valid(max_rating):
        books = books.filter(average_rating__lte=max_rating)

    sort = request.GET.get('sort')
    sort_query = sort_map.get(sort)
    if sort_query:
        order = request.GET.get('order')
        if not is_query_valid(order) or order != desc:
            books = books.order_by(sort_query)
        else:
            books = books.order_by('-' + sort_query)

    books = books[:50]

    if session_exists:
        session = get_session(request)
        if session:
            user = session.user
            books = books.annotate(
                my_rating=Subquery(BooksRating.objects.filter(user=user, book=OuterRef('pk')).values('rating')))
        else:
            session_exists = False

    context = {
        'books': books,
        'publishers': publishers,
        'options': sorting_options,
        'order_types': order_types,
        'session_exists': session_exists,
    }
    return render(request, 'reviews/home.html', context)


def search(request):
    return render(request, 'reviews/home.html')


def rate(request):
    user = get_user(request)
    book_id = request.POST['book_id']
    newRating = request.POST['rating']
    book = None
    if book_id:
        book = BooksData.objects.get(isbn__exact=book_id)

    if newRating and book and user:
        booksRating = BooksRating(user=user, book=book, rating=newRating)
        if not booksRating.id:
            booksRating.id = BooksRating.objects.latest('id').id + 1
        booksRating.save()
    return redirect('reviews-home')


def is_query_valid(param):
    return param is not None and param != ''


def get_data():
    with connection.cursor() as cursor:
        cursor.execute("select isbn, avg(rating) where ")
        data = cursor.fetchall()
    df = pd.DataFrame(data)
    return df


def get_user(request):
    session = get_session(request)
    if session:
        return session.user
    return None


def get_session(request):
    session_exists = request.session.exists(request.session.session_key)
    if session_exists:
        try:
            session = BooksSession.objects.get(session_key=request.session.session_key)
        except BooksSession.DoesNotExist:
            return None
        if session.expire_date > datetime.now().date():
            return session
    return None
