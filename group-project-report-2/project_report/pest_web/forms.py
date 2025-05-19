from django import forms
from .models import PlantType, PlantPart, Plant, PestDisease, SurveillanceRecord, Farm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PlantTypeForm(forms.ModelForm):
    class Meta:
        model = PlantType
        fields = ['name']

class PlantPartForm(forms.ModelForm):
    class Meta:
        model = PlantPart
        fields = ['name']

class FarmForm(forms.ModelForm):
    class Meta:
        model = Farm
        fields = ['farm_name', 'size_in_hectares', 'farm_type']
        widgets = {
            'farm_name': forms.TextInput(attrs={'class': 'form-control'}),
            'size_in_hectares': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'farm_type': forms.TextInput(attrs={'class': 'form-control'}),
        }

class PlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = ['name', 'plant_type', 'number_of_plants', 'location']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'plant_type': forms.Select(attrs={'class': 'form-control'}),
            'number_of_plants': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
        }

class PestDiseaseForm(forms.ModelForm):
    class Meta:
        model = PestDisease
        fields = ['name', 'affected_parts', 'recommended_frequency', 'description', 'plant_type']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'affected_parts': forms.Select(attrs={'class': 'form-control'}),
            'recommended_frequency': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'plant_type': forms.Select(attrs={'class': 'form-control'}),
        }

class SurveillanceRecordForm(forms.ModelForm):
    class Meta:
        model = SurveillanceRecord
        fields = ['plant', 'pest_disease', 'date_time', 'part_surveyed', 'result', 'notes']
        widgets = {
            'plant': forms.Select(attrs={'class': 'form-control'}),
            'pest_disease': forms.Select(attrs={'class': 'form-control'}),
            'date_time': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'part_surveyed': forms.Select(attrs={'class': 'form-control'}),
            'result': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['plant'].queryset = Plant.objects.filter(grower=user)
            user_plant_types = Plant.objects.filter(
                grower=user
            ).values_list('plant_type', flat=True).distinct()
            self.fields['pest_disease'].queryset = PestDisease.objects.filter(
                plant_type__in=user_plant_types
            )

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
