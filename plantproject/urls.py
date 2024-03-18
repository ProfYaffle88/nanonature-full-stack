from django.urls import path
from . import views
from .views import HomeView, ProjectView, ProjectCardView, ProjectCreateView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', views.About, name='about'),
    path('project/<int:pk>', ProjectView.as_view(), name='project-view'),
    path('project/<int:project_pk>/card/<int:pk>/', ProjectCardView.as_view(), name='project-card-view'),
    path('project/create/', ProjectCreateView.as_view(), name='project-create'),
]