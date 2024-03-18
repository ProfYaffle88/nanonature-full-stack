from .models import PlantProject, PlantProjectCard
from django import forms


class ProjectForm(forms.ModelForm):
    class Meta:
        model = PlantProject
        fields = ('title', 'image', 'about',)