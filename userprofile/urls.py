app_name = 'userprofile'

from django.urls import path, include
from . import views
from .views import UserProfileDetailView, CustomSignupView

urlpatterns = [
    path('signup/', CustomSignupView.as_view(), name='custom_signup'),
    path('profile/<int:pk>/', UserProfileDetailView.as_view(), name='user-profile'),
    path('plantproject/', include('plantproject.urls')),
]
