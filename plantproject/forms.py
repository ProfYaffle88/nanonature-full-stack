from django import forms
from .models import PlantProject, PlantProjectCard, Comment


class ProjectForm(forms.ModelForm):
    class Meta:
        model = PlantProject
        fields = ('title', 'image', 'about',)


class ProjectCardForm(forms.ModelForm):
    class Meta:
        model = PlantProjectCard
        fields = ('title', 'image', 'entry_body',)


class CommentForm(forms.ModelForm):
    """
    Form class for users to comment on a project card
    """
    class Meta:
        model = Comment
        fields = ('body',)