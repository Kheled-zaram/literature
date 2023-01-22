from datetime import datetime, timedelta

from django.shortcuts import render, redirect
from django.contrib import messages
from reviews.models import BooksUser, BooksSession
from reviews.views import get_user, get_session
from .LoginForm import LoginForm
from .forms import UserForm
from django.contrib.auth.hashers import make_password, check_password


def register(request):
    session_exists = get_session(request) is not None
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            sign_up = form.save(commit=False)
            sign_up.password = make_password(password=password)
            sign_up.save()
            messages.success(request, f'Account created for {username}.')
            return redirect('reviews-home')
    else:
        form = UserForm()
    return render(request, 'users/register.html', {'form': form, 'session_exists': session_exists,})


def login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.data is not None:
            username = form.data.get('username')
            password = form.data.get('password')
            if username and password:
                user = BooksUser.objects.get(username=username)
                if user and check_password(password, user.password):
                    messages.success(request, f'User {username} has signed in.')
                    if not request.session.exists(request.session.session_key):
                        request.session.create()
                    key = request.session.session_key
                    date = datetime.now() + timedelta(days=1)
                    session = BooksSession(user=user, session_key=key, expire_date=date)
                    session.save()
                    return redirect('reviews-home')
        messages.info(request, f'Invalid username or password.')
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})


def logout(request):
    session = get_session(request)
    if session:
        session.delete()
    return redirect('reviews-home')
