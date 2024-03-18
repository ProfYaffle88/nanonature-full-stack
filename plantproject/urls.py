from django.urls import path
from . import views
from .views import HomeView, ProjectView, ProjectCardView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', views.About, name='about'),
    path('project/<int:pk>', ProjectView.as_view(), name='project-view'),
    path('project/<int:project_pk>/card/<int:card_pk>/', ProjectCardView.as_view(), name='project-card-view'),
]