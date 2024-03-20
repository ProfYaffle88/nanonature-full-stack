from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import DetailView
from django.contrib.auth.views import LoginView, FormView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

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


class CustomSignupView(FormView):
    """
    View for displaying custom signup form that updates User
    """
    template_name = 'signup.html'
    form_class = SignupForm
    success_url = 'userprofile:custom_profile'
    
    print("Success URL:", success_url)
    
    def form_valid(self, form):        
        user = form.save()
        login(self.request, user)
        return HttpResponseRedirect(self.success_url)


class CustomProfileView(LoginView):
    """
    View for displaying custom signup form that updates UserProfile after User creation
    """
    template_name = 'create_user_profile.html'
    form_class = SignupForm

    def form_valid(self, form):
        user = form.save()
        return HttpResponseRedirect(self.get_success_url())


@login_required
def edit_profile(request):
    user = request.user
    if request.method == 'POST':
        user_form = SignupForm(request.POST, instance=user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('user-profile', pk=user.pk)
    else:
        user_form = SignupForm(instance=user)
        profile_form = UserProfileForm(instance=user.userprofile)
    return render(request, 'edit_profile.html', {'user_form': user_form, 'profile_form': profile_form})


@login_required
def delete_user(request):
    if request.method == 'POST':
        request.user.delete()
        # Redirect to confirmation page or logout
        logout(request)
        return redirect('/')  # Redirect to home page after logout

    return render(request, 'delete_user.html')  # Render a confirmation page with a delete button