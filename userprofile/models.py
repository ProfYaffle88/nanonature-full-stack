from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from plantproject.models import PlantProject

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = CloudinaryField('image')
    bio = models.TextField()
    projects = models.ManyToManyField(PlantProject, related_name='user_profiles')
