import django_filters
from .models import BooksData

class ReviewsFilter(django_filters.FilterSet):

    class Meta:
        model = BooksData
        fields = ('publisher', 'year')