from django.db import models
from django.contrib.auth.models import User
    
    
class PlantPart(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name
    
class PestDisease(models.Model):
    identifier = models.IntegerField(
        null=False,
        blank=False,
        unique=True,
        default=1,  # Temporary default for migration
    )
    name = models.CharField(max_length=100)
    scientific_name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image_url = models.URLField(blank=True)  # Changed to URLField for better validation
    image_reference = models.TextField(blank=True)
    symptoms = models.TextField()
    prevention = models.TextField()
    treatment = models.TextField()
    affected_parts = models.ManyToManyField(PlantPart)  # Changed to ManyToMany as a pest can affect multiple parts
    recommended_frequency = models.CharField(max_length=100)
    plant_type = models.CharField(max_length=100)  # Using CharField for now, can be ForeignKey if you create PlantType model
    
    def __str__(self):
        return self.name












class Farm(models.Model):
    grower = models.OneToOneField(User, on_delete=models.CASCADE)
    farm_name = models.CharField(max_length=200)
    size_in_hectares = models.FloatField()
    farm_type = models.CharField(max_length=200)
    
    def __str__(self):
        return f"{self.farm_name} ({self.grower.username})"


# Dynamic lists
# class PlantType(models.Model):
#     name = models.CharField(max_length=100, unique=True)
    
#     def __str__(self):
#         return self.name

# class PlantPart(models.Model):
#     name = models.CharField(max_length=100, unique=True)
    
#     def __str__(self):
#         return self.name

# # Farm model linked to grower
# class Farm(models.Model):
#     grower = models.OneToOneField(User, on_delete=models.CASCADE)
#     farm_name = models.CharField(max_length=100)
#     size_in_hectares = models.FloatField()
#     farm_type = models.CharField(max_length=100)

#     def __str__(self):
#         return f"{self.farm_name} ({self.grower.username})"

# # Main Plant model
# class Plant(models.Model):
#     grower = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
#     name = models.CharField(max_length=100)
#     plant_type = models.ForeignKey(PlantType, on_delete=models.CASCADE)
#     number_of_plants = models.PositiveIntegerField()
#     location = models.CharField(max_length=150)

#     def __str__(self):
#         return f"{self.name} ({self.plant_type})"

# # class PestDisease(models.Model):
# #     name = models.CharField(max_length=100)
# #     affected_parts = models.ForeignKey(PlantPart, on_delete=models.CASCADE)
# #     recommended_frequency = models.CharField(max_length=100)
# #     description = models.TextField(blank=True)
# #     plant_type = models.ForeignKey(PlantType, on_delete=models.CASCADE)

# #     def __str__(self):
# #         return self.name

# class PestDisease(models.Model):
#     identifier = models.IntegerField(
#         null=False,
#         blank=False,
#         unique=True,
#         default=1,  # Temporary default for migration
#     )
#     name = models.CharField(max_length=100,default="")
#     scientific_name = models.CharField(max_length=100,default="")
#     description = models.TextField(blank=False,default="")
#     image_url = models.TextField(blank=False,default="") # Used Text Field to simplify dir
#     image_reference = models.TextField(blank=False,default="")
#     symptoms = models.TextField(blank=False,default="")
#     prevention = models.TextField(blank=False,default="")
#     treatment= models.TextField(blank=False,default="")
#     ## Need Corrections 
#     affected_parts = models.ForeignKey(PlantPart, on_delete=models.CASCADE)
#     recommended_frequency = models.CharField(max_length=100,default="")
#     description = models.TextField(blank=True,default="")
#     plant_type = models.ForeignKey(PlantType, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.name

# # Surveillance records for each grower's plant
# class SurveillanceRecord(models.Model):
#     grower = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
#     plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
#     pest_disease = models.ForeignKey(PestDisease, on_delete=models.CASCADE)
#     date_time = models.DateTimeField()
#     part_surveyed = models.ForeignKey(PlantPart, on_delete=models.CASCADE)
#     result = models.TextField()
#     notes = models.TextField(blank=True)

#     def __str__(self):
#         return f"Surveillance by {self.grower.username} on {self.date_time.strftime('%Y-%m-%d')}"
