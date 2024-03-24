from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import PlantProject, PlantProjectCard, Comment
from .forms import ProjectForm, ProjectCardForm, CommentForm


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
    ``comments``
        All comments related to the project card.
    ``comment_count``
        A count of comments related to the project card.
    ``comment_form``
        An instance of :form:`plantproject.CommentForm`.

    **Template:**
    :template:`plantproject/project_card_view.html`
    """
    model = PlantProjectCard
    template_name = 'plantproject/project_card_view.html'
    comment_form = CommentForm()

    def get_object(self, queryset=None):
        project_pk = self.kwargs.get('project_pk')
        card_pk = self.kwargs.get('card_pk')
        # Fetch the PlantProjectCard object using project_pk and card_pk
        obj = get_object_or_404(PlantProjectCard, project__pk=project_pk, pk=card_pk)
        return obj
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project_card = self.object
        project = project_card.project
        context['project'] = project
        context['prev_card'] = project.project_cards.filter(created_on__lt=project_card.created_on).order_by('-created_on').first()
        context['next_card'] = project.project_cards.filter(created_on__gt=project_card.created_on).order_by('created_on').first()
        # Fetching comments related to the project card
        context['comments'] = project_card.comments.all().order_by("-created_on")
        context['comment_count'] = project_card.comments.count()
        # Fetch comment form
        context['comment_form'] = self.comment_form
        return context

    def post(self, request, *args, **kwargs):
        # Handle POST request for adding a comment
        project_pk = self.kwargs.get('project_pk')
        card_pk = self.kwargs.get('card_pk')
        project_card = get_object_or_404(PlantProjectCard, project__pk=project_pk, pk=card_pk)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.card = project_card
            comment.save()
            messages.success(request, 'Comment submitted!')
            return HttpResponseRedirect(reverse('project-card-view', kwargs={'project_pk': project_pk, 'card_pk': card_pk}))
        else:
            messages.error(request, 'Error submitting comment!')
            return self.get(request, *args, **kwargs)



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

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

    # if successful, navigate to newly created project
    def get_success_url(self):
        return reverse('project-view', kwargs={'pk': self.object.pk})


class ProjectCardCreateView(CreateView):
    model = PlantProjectCard
    fields = ['title', 'image', 'entry_body',]
    template_name = 'plantproject/project_card_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project_pk = self.kwargs.get('project_pk')
        project = get_object_or_404(PlantProject, pk=project_pk)
        context['project'] = project
        return context
    
    def form_valid(self, form):
        project_pk = self.kwargs.get('project_pk')
        project = get_object_or_404(PlantProject, pk=project_pk)
        form.instance.project = project
        return super().form_valid(form)

    # if successful, navigate to newly created project
    def get_success_url(self):
        project_pk = self.object.project.pk
        return reverse('project-card-view', kwargs={'project_pk': project_pk, 'card_pk': self.object.pk})


def comment_edit(request, project_pk, card_pk, comment_pk):
    """
    Display an individual comment for edit.

    **Context**

    ``card``
        An instance of :model:`plantproject.PlantProjectCard`.
    ``comment``
        A single comment related to the card.
    ``comment_form``
        An instance of :form:`plantproject.CommentForm`
    """
    if request.method == "POST":
        card = get_object_or_404(PlantProjectCard, pk=card_pk)
        comment = get_object_or_404(Comment, pk=comment_pk)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save()
            comment.card = card
            comment.save()
            messages.success(request, 'Comment Updated!')
        else:
            messages.error(request, 'Error updating comment!')

    return HttpResponseRedirect(reverse('project-card-view', kwargs={'project_pk': project_pk, 'card_pk': card_pk}))

def comment_delete(request, project_pk, card_pk, comment_pk):
    """
    Delete an individual comment.

    **Context**

    ``card``
        An instance of :model:`plantproject.PlantProjectCard`.
    ``comment``
        A single comment related to the project card.
    """
    card = get_object_or_404(PlantProjectCard, pk=card_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)

    if comment.author == request.user:
        comment.delete()
        messages.success(request, 'Comment deleted!')
    else:
        messages.error(request, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('project-card-view', kwargs={'project_pk': project_pk, 'card_pk': card_pk}))


def delete_project(request, project_pk):
    project = get_object_or_404(PlantProject, pk=project_pk)
    project.delete()
    return HttpResponseRedirect(reverse('home'))

    # if request.user == project.creator:
    #     if request.method == 'POST':
    #         project.delete()
    #         return redirect('userprofile:user-profile', pk=request.user.pk)
    #     else:
    #         return redirect('project-view', pk=project_pk)
    # else:
    #     return render(request, 'error_page.html', {'message': 'You are not authorized to delete this project.'})


class EditProjectView(UpdateView):
    """
    Edit an existing project
    """
    model = PlantProject
    fields = ['title', 'image', 'about']
    pk_url_kwarg = 'project_pk'
    template_name = 'plantproject/edit_project.html'
    
    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('project-detail', kwargs={'project_pk': self.object.pk})


def delete_project_card(request, project_pk, card_pk):
    project = get_object_or_404(PlantProject, pk=project_pk)
    card = get_object_or_404(PlantProjectCard, pk=card_pk)
    card.delete()
    return HttpResponseRedirect(reverse('project-view', kwargs={'project_pk': project_pk}))


class edit_project_card(UpdateView):
    """
    Edit an exisiting entry in a project
    """
    model = PlantProjectCard
    template_name ='edit_project_card.html'
    form_class = ProjectCardForm