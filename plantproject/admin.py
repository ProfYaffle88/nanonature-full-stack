from django.contrib import admin
from .models import PlantProject, PlantProjectCard

admin.site.register(PlantProject, PlantProjectCard)