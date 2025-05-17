from django.contrib import admin

# Register your models here.
from .models import PlantType, PlantPart, Plant, PestDisease, SurveillanceRecord

myModels = [PlantType, PlantPart, Plant, PestDisease, SurveillanceRecord]
admin.site.register(myModels)

