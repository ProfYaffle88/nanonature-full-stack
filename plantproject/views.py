from django.views.generic import ListView, DetailView
from django.shortcuts import render


def index(request):
    return render(request, 'plantproject/index.html')
