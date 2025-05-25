from django import forms
from .models import PestDisease, PlantPart, Farm, SurveillanceRecord, Tree
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PestDiseaseForm(forms.ModelForm):
    class Meta:
        model = PestDisease
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Make fields more user-friendly for the target age group
        self.fields['description'].widget = forms.Textarea(attrs={'rows': 3})
        self.fields['symptoms'].widget = forms.Textarea(attrs={'rows': 3})
        self.fields['prevention'].widget = forms.Textarea(attrs={'rows': 3})
        self.fields['treatment'].widget = forms.Textarea(attrs={'rows': 3})

class PlantPartForm(forms.ModelForm):
    class Meta:
        model = PlantPart
        fields = '__all__'

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class FarmForm(forms.ModelForm):
    class Meta:
        model = Farm
        fields = ['farm_name', 'size_in_hectares', 'farm_type']

#Tree Form  
class TreeForm(forms.ModelForm):
    class Meta:
        model = Tree
        fields = ['tag_number', 'variety', 'planting_date', 'location_description', 'notes']
        widgets = {
            'tag_number': forms.TextInput(attrs={
        'placeholder': 'Tree ID' }),
            'variety': forms.TextInput(attrs={
        'placeholder': 'Mango cultivar/variety' }),
            'planting_date': forms.DateInput(attrs={'type': 'date'}),
            'notes': forms.Textarea(attrs={'rows': 3}),
            'location_description': forms.TextInput(attrs={
        'placeholder': 'e.g., North field, row 3'
    }), 
        'notes': forms.TextInput(attrs={
        'placeholder': 'General notes about the tree'
        }),
        }


class SurveillanceRecordForm(forms.ModelForm):
    class Meta:
        model = SurveillanceRecord
        fields = ['tree', 'pest_disease', 'affected_plant_part', 'severity', 'notes', 'time_spent']
    
        widgets = {
            'notes': forms.Textarea(attrs={'rows': 3}),
            'time_spent': forms.TextInput(attrs={'placeholder': 'HH:MM:SS'}),
        }
        
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        
        if user and user.farm:
            self.fields['tree'].queryset = Tree.objects.filter(farm=user.farm)
 
 
#  25 05 2025 - Before tree reference expansion         
# class SurveillanceRecordForm(forms.ModelForm):
#     class Meta:
#         model = SurveillanceRecord
#         fields = ['pest_disease', 'affected_plant_part', 'severity', 'notes']
#         widgets = {
#             'notes': forms.Textarea(attrs={'rows': 3}),
#         }

#     def __init__(self, *args, **kwargs):
#         user = kwargs.pop('user', None)
#         super().__init__(*args, **kwargs)
#         if user and hasattr(user, 'farm'):
#             self.fields['pest_disease'].queryset = PestDisease.objects.all()
#             self.fields['affected_plant_part'].queryset = PlantPart.objects.all()
