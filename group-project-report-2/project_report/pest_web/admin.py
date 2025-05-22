from django.contrib import admin

# Register your models here.
from .models import PlantPart, PestDisease

# myModels = [PlantType, PlantPart, Plant, PestDisease, SurveillanceRecord]
myModels = [PlantPart, PestDisease]
admin.site.register(myModels)


