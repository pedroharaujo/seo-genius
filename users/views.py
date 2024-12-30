from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView


def signup(request):
    return render(request, 'users/signup.html')


def login(request):
    return render(request, 'users/login.html')
