from django.urls import path
from . import views
from .views import HomeView, ProjectView, ProjectCardView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', views.About, name='about'),
    path('project/<int:pk>', ProjectView.as_view(), name='project-view'),
    path('project/<int:pk>/card/<int:pk>/', ProjectCardView.as_view(), name='project-card-view'),
]