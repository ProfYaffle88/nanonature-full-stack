app_name = 'userprofile'

from django.urls import path, include
from . import views
from .views import UserProfileDetailView, CustomProfileView, edit_profile, delete_user

urlpatterns = [
    # path('signup/', CustomSignupView.as_view(), name='custom_signup'),
    path('signup/create-profile/', CustomProfileView.as_view(), name='custom_profile'),
    path('profile/<int:pk>/', UserProfileDetailView.as_view(), name='user-profile'),
    path('profile/<int:pk>/edit-profile/', views.edit_profile, name='edit-profile'),
    path('delete-user/', views.delete_user, name='delete-user'),
    path('plantproject/', include('plantproject.urls')),
]
