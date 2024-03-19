from .models import PlantProject, PlantProjectCard, Comment
from django import forms


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
        """
        Specify the django model and order of the fields
        """
        model = Comment
        fields = ('body',)