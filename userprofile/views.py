from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, FormView
from django.contrib.auth.views import LoginView, FormView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import SignupForm, UserProfileForm
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
        # Get the user's profile
        user_profile = self.get_object()
        context['user_is_owner'] = user_profile.user == self.request.user
        # Get the user's projects
        user_projects = PlantProject.objects.filter(creator=self.object.user)
        context['projects'] = user_projects
        return context


class CustomProfileView(LoginRequiredMixin, FormView):
    """
    View for displaying custom signup form that updates UserProfile after User creation
    """
    template_name = 'userprofile/create_user_profile.html'
    form_class = UserProfileForm
    success_url = '/'

    def form_valid(self, form):
        user_profile = form.save(commit=False)
        user_profile.user = self.request.user
        user_profile.save()
        return redirect(self.get_success_url())


@login_required
def edit_profile(request, pk):
    user = request.user
    user_profile = get_object_or_404(UserProfile, user=request.user)

    if request.user.pk != pk and not request.user.is_superuser:
        return render(request, '403.html', status=403)

    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, request.FILES, instance=user.userprofile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('userprofile:user-profile', pk=user.pk)
        else:
            print("Form is invalid")
            print(profile_form.errors)
    else:
        profile_form = UserProfileForm(instance=user.userprofile)
    return render(request, 'userprofile/edit_profile.html', {'profile_form': profile_form})


@login_required
def delete_user(request):
    if request.method == 'POST':
        if request.user == request.user or request.user.is_superuser:
            request.user.delete()
            logout(request)
            return redirect('/')
        else:
            return render(request, '403.html', status=403)
    else:
        return redirect('userprofile:user-profile', pk=request.user.pk)