from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from reviews.models import BooksUser
from .forms import UserForm


def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            messages.success(request, f'Account created for {username}.')
            return redirect('reviews-home')
    else:
        form = UserForm()
    return render(request, 'users/register.html', {'form': form})
