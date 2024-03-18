from django.urls import path
from . import views
from .views import HomeView, ProjectView, ProjectCardView, ProjectCreateView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', views.About, name='about'),
    path('project/create/', ProjectCreateView.as_view(), name='project-create'),
    path('project/<int:project_pk>/create-card/', ProjectCardCreateView.as_view(), name='project-card-create'),
    path('project/<int:project_pk>/card/<int:card_pk>/', ProjectCardView.as_view(), name='project-card-view'),
    path('project/<int:pk>/', ProjectView.as_view(), name='project-view'),
]