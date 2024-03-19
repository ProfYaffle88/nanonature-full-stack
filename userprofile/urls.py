app_name = 'userprofile'

from django.urls import path
from . import views
from .views import UserProfileDetailView

urlpatterns = [
    path('profile/<int:pk>/', UserProfileDetailView.as_view(), name='user-profile'),
]
