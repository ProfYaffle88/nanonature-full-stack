from django import forms
from .models import PlantProject, PlantProjectCard, Comment


class ProjectForm(forms.ModelForm):
    class Meta:
        model = PlantProject
        fields = ('title', 'image', 'about',)

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        self.fields[
            'image'
            ].label = "You can upload an image here"


class ProjectCardForm(forms.ModelForm):
    class Meta:
        model = PlantProjectCard
        fields = ('title', 'image', 'entry_body',)

    def __init__(self, *args, **kwargs):
        super(ProjectCardForm, self).__init__(*args, **kwargs)
        self.fields[
            'image'
            ].label = "You can upload an image here"


class CommentForm(forms.ModelForm):
    """
    Form class for users to comment on a project card
    """
    class Meta:
        model = Comment
        fields = ('body',)