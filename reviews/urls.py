from django.urls import path, include
from . import views
from users import views as user_views

urlpatterns = [
    path('', views.home, name='reviews-home'),
    path('register/', user_views.register, name='register'),
    path('login/', user_views.login, name='login'),
    path('logout/', user_views.logout, name='logout'),
    path('search/', views.search, name='search'),
    path('rate/', views.rate, name='rate'),
]