#modelform classes for models to use in views 
from django import forms 
from .models import Plant, PestDisease, SurveillanceRecord 

class PlantForm(froms.ModelForm):
    class Meta:
        model = Plant 
        fields = '__all__'
        
class PestDiseaseForm(forms.ModelForm):
    class Meta:
        model = Plant 
        fields = '__all__'
        
class SurveillanceRecordForm(forms.ModelForm):
    class Meta:
        model = SurveillanceRecord
        fields = '__all__'
        