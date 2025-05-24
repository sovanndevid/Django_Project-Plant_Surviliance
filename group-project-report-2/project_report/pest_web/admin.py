from django.contrib import admin

# Register your models here.
from .models import PestDisease, PlantPart, Farm, SurveillanceRecord

myModels = [PestDisease, PlantPart, Farm, SurveillanceRecord]
admin.site.register(myModels)

