from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import render, get_object_or_404, reverse
from .models import PlantProject, PlantProjectCard
from .forms import ProjectForm


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
    """
    Displays details of a single project and all cards within.

    **Context**
     ``plantproject``
        An instance of :model:`plantproject.PlantProject`
    ``project_card``
        An instance of :model:`plantproject.PlantProjectCard`.
    
    """
    model = PlantProject
    template_name = 'plantproject/project_view.html'

    # Fetch related PlantProjectCards for the current PlantProject
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project = self.object
        context['project'] = project
        context['project_cards'] = project.project_cards.all()
        return context


class ProjectCardView(DetailView):
    """
    Displays details of a single project card within a project.

    **Context**
    ``project_card``
        An instance of :model:`plantproject.PlantProjectCard`.
    
    """
    model = PlantProjectCard
    template_name = 'plantproject/project_card_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project_card = self.object
        project = project_card.project
        context['project'] = project
        context['prev_card'] = project.project_cards.filter(created_on__lt=project_card.created_on).order_by('-created_on').first()
        context['next_card'] = project.project_cards.filter(created_on__gt=project_card.created_on).order_by('created_on').first()
        return context


def About(request):
    """
    Renders the about page.

    **Template:**
    :template:`plantproject/about.html`
    """
    return render(request, 'plantproject/about.html')


class ProjectCreateView(CreateView):
    model = PlantProject
    fields = ['title', 'image', 'about']
    template_name = 'plantproject/project_create.html'

    # if successful, navigate to newly created project
    def get_success_url(self):
        return reverse('project-view', kwargs={'pk': self.object.pk})