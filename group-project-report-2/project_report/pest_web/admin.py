from django.contrib import admin

# Register your models here.
from .models import PlantType, PlantPart, Farm

myModels = [PlantType, PlantPart, Farm]
admin.site.register(myModels)

