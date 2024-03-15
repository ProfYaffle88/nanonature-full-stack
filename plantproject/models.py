from django.db import models
from cloudinary.models import CloudinaryField

class PlantProject(models.Model):
    title = models.CharField(max_length=100)
    image = CloudinaryField('image', default='placeholder')
    about = models.TextField()
    project_card_entries = models.ForeignKey(PlantProjectCard)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)
