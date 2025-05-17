from django.contrib import admin

# Register your models here.
from .models import PlantType, PlantPart, Plant, PestDisease, SurveillanceRecord

admin.site.register(PlantType)
admin.site.register(PlantPart)
admin.site.register(Plant)
admin.site.register(PestDisease)
admin.site.register(SurveillanceRecord)

