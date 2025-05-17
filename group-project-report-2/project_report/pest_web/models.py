from django.db import models 

#dynamic lists 
class PlantType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name 
    
class PlantPart(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name 
    
#main models for the pests 

class Plant(models.Model):
    name = models.CharField(max_length=100)
    plant_type = models.ForeignKey(PlantType, on_delete=models.CASCADE)
    number_of_plants = models.PositiveIntegerField()
    location = models.CharField(max_length=150)
    
    def __str__(self):
        return f"{self.name} ({self.plant_type})"
    
class PestDisease(models.Model):
    name = models.CharField(max_length=100)
    affected_parts = models.ForeignKey(PlantPart, on_delete=models.CASCADE)
    recommended_frequency = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    plant_type = models.ForeignKey(PlantType, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name 
# for record on plant parts  
class SurveillanceRecord(models.Model):
    grower_name = models.CharField(max_length=100)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    pest_disease = models.ForeignKey(PestDisease, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    part_surveyed = models.ForeignKey(PlantPart, on_delete=models.CASCADE)
    result = models.TextField()
    notes = models.TextField(blank=True)
    
    def __str__(self):
        return f"Surveillance by {self.grower_name} on {self.date_time.strftime('%Y-%m-%d')}"
    

        