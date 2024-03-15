from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.shortcuts import render


def home(request):
    return render(request, 'home.html', {})
