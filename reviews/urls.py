from django.urls import path, include
from . import views
from users import views as user_views

urlpatterns = [
    path('', views.home, name='reviews-home'),
    path('about/', views.about, name='reviews-about'),
    path('register/', user_views.register, name='register'),
    path('search/', views.search, name='search')
]