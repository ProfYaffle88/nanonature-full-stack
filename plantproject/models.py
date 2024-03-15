from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class PlantProject(models.Model):
    """
    Stores a single user project, related to :model:`auth.User` and :model:`plantproject.PlantProjectCards`
    """
    creator = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="project_creator"
    )
    title = models.CharField(max_length=200, unique=True)
    image = CloudinaryField('image', default='placeholder')
    about = models.TextField(default="Tell everyone about your project!")
    project_card_entries = models.ForeignKey(
        'PlantProjectCard', on_delete=models.CASCADE, related_name="plant_project_cards"
        )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]
    
    def __str__(self):
        return f"Project: {self.title} | a project by {self.creator}"



class PlantProjectCard(models.Model):
    """
    Stores a single entry to a project, related to :model:`plantproject.PlantProject`
    """
    title = models.CharField(max_length=200, unique=True)
    image = CloudinaryField('image', default='placeholder')
    entry_body = models.TextField(default="Tell everyone about the update to your project!")
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"Project Entry: {self.title}"