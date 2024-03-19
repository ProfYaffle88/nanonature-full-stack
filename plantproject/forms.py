from .models import PlantProject, PlantProjectCard
from django import forms


class ProjectForm(forms.ModelForm):
    class Meta:
        model = PlantProject
        fields = ('title', 'image', 'about',)


class ProjectCardForm(forms.ModelForm):
    class Meta:
        model = PlantProjectCard
        fields = ('title', 'image', 'entry_body',)