from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.shortcuts import render
from .models import PlantProject


class HomeView(ListView):
    queryset = PlantProject.objects.all()
    template_name = 'plantproject/home.html'
    paginate_by = 8
