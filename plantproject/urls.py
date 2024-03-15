from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProjectList, name='home'),
]