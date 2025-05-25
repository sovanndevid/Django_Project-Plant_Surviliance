from django.contrib import admin

# Register your models here.
from .models import PestDisease, PlantPart, Farm, SurveillanceRecord, Tree

myModels = [PestDisease, PlantPart, Farm, SurveillanceRecord, Tree]
admin.site.register(myModels)

