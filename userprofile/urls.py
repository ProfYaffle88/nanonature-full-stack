app_name = 'userprofile'

from django.urls import path, include
from . import views
from .views import UserProfileDetailView, CustomSignupView, edit_profile, delete_user

urlpatterns = [
    path('signup/', CustomSignupView.as_view(), name='custom_signup'),
    path('profile/<int:pk>/', UserProfileDetailView.as_view(), name='user-profile'),
    path('edit-profile/', views.edit_profile, name='edit-profile'),
    path('delete-user/', views.delete_user, name='delete-user'),
    path('plantproject/', include('plantproject.urls')),
]
