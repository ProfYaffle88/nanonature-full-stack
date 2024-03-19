from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from django.contrib.auth.views import LoginView
from .forms import SignupForm
from .models import UserProfile
from plantproject.models import PlantProject

class UserProfileDetailView(DetailView):
    """
    View for displaying user profile details.
    """
    model = UserProfile
    template_name = 'userprofile/user_profile.html'
    context_object_name = 'profile'

    def get_object(self, queryset=None):
        # Retrieve the UserProfile object associated with the user's primary key
        pk = self.kwargs.get('pk')
        return get_object_or_404(UserProfile, user_id=pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get the user's projects
        user_projects = PlantProject.objects.filter(creator=self.object.user)
        context['projects'] = user_projects
        return context


class CustomSignupView(LoginView):
    """
    View for displaying custom signup form that updates both User and UserProfile
    """
    template_name = 'signup.html'
    form_class = SignupForm

    def form_valid(self, form):
        user = form.save(commit=False)
        user.save()
        
        bio = form.cleaned_data.get('bio')
        image = form.cleaned_data.get('image')
        UserProfile.objects.create(user=user, bio=bio, image=image)

        return HttpResponseRedirect(self.get_success_url())
