from django.contrib import admin

# Register your models here.
from .models import PestDisease, PlantPart, Farm

myModels = [PestDisease, PlantPart, Farm]
admin.site.register(myModels)

