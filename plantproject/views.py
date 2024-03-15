from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.shortcuts import render
from .models import PlantProject


class HomeView(ListView):
    """
    Class-based view of all projects, ordered by most recent.

    **Context**
    ``plantproject``
        An instance of :model:`plantproject.PlantProject`
    
    """
    queryset = PlantProject.objects.all()
    template_name = 'plantproject/home.html'
    paginate_by = 8


class ProjectView(DetailView):
    model = PlantProject
    template_name = 'project_view.html'


def About(request):
    """
    Renders the about page.

    **Template:**
    :template:`plantproject/about.html`
    """
    return render(request, 'plantproject/about.html')