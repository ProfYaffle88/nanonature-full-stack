from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import UserProfile
from plantproject.models import PlantProject

class UserProfileDetailView(DetailView):
    """
    View for displaying user profile details.
    """
    model = UserProfile
    template_name = 'user_profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get the user's projects
        user_projects = Project.objects.filter(user=self.object.user)
        context['projects'] = user_projects
        return context
