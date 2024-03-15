from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.shortcuts import render


class HomeView(generic.Listview):
    queryset = PlantProject.objects.all()
    template_name = 'home.html'
    paginate_by = 8
