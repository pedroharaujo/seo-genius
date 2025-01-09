from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect


def signup(request):
    return render(request, 'users/signup.html')


def login(request):
    return render(request, 'users/login.html')


@login_required
def dashboard(request):
    return render(request, 'users/dashboard.html', {
        'user': request.user,
    })
