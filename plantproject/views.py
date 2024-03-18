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
    
    # Fetch related PlantProjectCards for the current PlantProject
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project_cards'] = self.object.plant_project_cards.all()
        return context


def About(request):
    """
    Renders the about page.

    **Template:**
    :template:`plantproject/about.html`
    """
    return render(request, 'plantproject/about.html')