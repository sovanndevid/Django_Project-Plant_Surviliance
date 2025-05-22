from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import JsonResponse
from django.db.models import Q
from django.utils import timezone

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import PestDisease, PlantPart, Farm
from .forms import PestDiseaseForm, PlantPartForm, FarmForm, UserRegisterForm


# Displaying a list of 7 pest diseases
class PestDiseaseListView(ListView):
    model = PestDisease
    template_name = 'pests/plist.html'
    context_object_name = 'pests'
    paginate_by = 7 

# Displaying home page at localhost/ link 
class HomeView(TemplateView):
    """Home page view"""
    template_name = 'pests/home.html'
    
    
class AboutView(TemplateView):
    """About page view"""
    template_name = 'pests/about.html'


def register(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        farm_form = FarmForm(request.POST)

        if user_form.is_valid() and farm_form.is_valid():
            user = user_form.save()
            farm = farm_form.save(commit=False)
            farm.grower = user
            farm.save()
            messages.success(request, "Registration successful.")
            return redirect('login')
    else:
        user_form = UserRegisterForm()
        farm_form = FarmForm()
    
    return render(request, 'pests/register.html', {
        'user_form': user_form,
        'farm_form': farm_form
    })
# View for logged-in users to see their farm info
@login_required
def farm_profile(request):
    farm = get_object_or_404(Farm, grower=request.user)
    return render(request, 'pests/farm_profile.html', {'farm': farm})

# Edit farm info
@login_required
def edit_farm(request):
    farm = get_object_or_404(Farm, grower=request.user)
    if request.method == 'POST':
        form = FarmForm(request.POST, instance=farm)
        if form.is_valid():
            form.save()
            messages.success(request, "Farm updated.")
            return redirect('pests/farm_profile')
    else:
        form = FarmForm(instance=farm)
    return render(request, 'pests/edit_farm.html', {'form': form})



 
        
# from .forms import (
#     PlantTypeForm,
#     PlantPartForm,
#     PlantForm,
#     PestDiseaseForm,
#     SurveillanceRecordForm,
#     UserRegisterForm,
# )
 
# Authentication Views
# def register(request):
#     if request.method == 'POST':
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Account created for {username}! You can now log in.')
#             return redirect('login')
#     else:
#         form = UserRegisterForm()
#     return render(request, 'pests/register.html', {'form': form})
 
# # Home View
# class HomeView(TemplateView):
#     template_name = 'pests/home.html'
 
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         if self.request.user.is_authenticated:
#             context['recent_surveys'] = SurveillanceRecord.objects.filter(
#                 grower=self.request.user
#             ).order_by('-date_time')[:5]
#         return context

# # Pest/Disease Views
# class PestDiseaseListView(LoginRequiredMixin, ListView):
#     model = PestDisease
#     template_name = 'pests/plist.html'
#     context_object_name = 'pests'
 
#     def get_queryset(self):
#         user_plant_types = Plant.objects.filter(
#             grower=self.request.user
#         ).values_list('plant_type', flat=True).distinct()
#         return PestDisease.objects.filter(plant_type__in=user_plant_types) 
 
# class PestDiseaseDetailView(LoginRequiredMixin, DetailView):
#     model = PestDisease
#     template_name = 'pests/details.html'
  
# # Plant Type Views
# class PlantTypeListView(LoginRequiredMixin, ListView):
#     model = PlantType
#     template_name = 'pests/planttype_list.html'
#     context_object_name = 'plant_types'
 
# class PlantTypeCreateView(LoginRequiredMixin, CreateView):
#     model = PlantType
#     form_class = PlantTypeForm
#     template_name = 'pests/planttype_form.html'
#     success_url = reverse_lazy('plant-type-list')
 
# class PlantTypeUpdateView(LoginRequiredMixin, UpdateView):
#     model = PlantType
#     form_class = PlantTypeForm
#     template_name = 'pests/planttype_form.html'
#     success_url = reverse_lazy('plant-type-list')
 
# # Plant Views
# class PlantListView(LoginRequiredMixin, ListView):
#     model = Plant
#     template_name = 'pests/plant_list.html'
 
#     def get_queryset(self):
#         return Plant.objects.filter(grower=self.request.user)
 
# class PlantCreateView(LoginRequiredMixin, CreateView):
#     model = Plant
#     form_class = PlantForm
#     template_name = 'pests/plant_form.html'
#     success_url = reverse_lazy('plant-list')
 
#     def form_valid(self, form):
#         form.instance.grower = self.request.user
#         return super().form_valid(form)
 
# class PlantDetailView(LoginRequiredMixin, DetailView):
#     model = Plant
#     template_name = 'pests/plant_detail.html'
 
# # Surveillance Views
# class SurveillanceCreateView(LoginRequiredMixin, CreateView):
#     model = SurveillanceRecord
#     form_class = SurveillanceRecordForm
#     template_name = 'pests/surveillance_form.html'
#     success_url = reverse_lazy('surveillance-list')
 
#     def get_form_kwargs(self):
#         kwargs = super().get_form_kwargs()
#         kwargs['user'] = self.request.user
#         return kwargs
 
#     def form_valid(self, form):
#         form.instance.grower = self.request.user
#         return super().form_valid(form)
 
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         if 'plant' in self.request.GET:
#             plant_id = self.request.GET.get('plant')
#             try:
#                 plant = Plant.objects.get(id=plant_id, grower=self.request.user)
#                 effort = plant.number_of_plants * 2  # 2 minutes per plant
#                 context['estimated_effort'] = f"{effort} minutes for {plant.number_of_plants} plants"
#             except Plant.DoesNotExist:
#                 pass
#         return context
 
# class SurveillanceListView(LoginRequiredMixin, ListView):
#     model = SurveillanceRecord
#     template_name = 'pests/surveillance_list.html'
 
#     def get_queryset(self):
#         return SurveillanceRecord.objects.filter(
#             grower=self.request.user
#         ).order_by('-date_time')
 
# class SurveillanceDetailView(LoginRequiredMixin, DetailView):
#     model = SurveillanceRecord
#     template_name = 'pests/surveillance_detail.html'
 
# # AJAX View for dynamic forms
# @login_required
# def get_pests_for_plant(request):
#     plant_id = request.GET.get('plant_id')
#     plant = get_object_or_404(Plant, id=plant_id, grower=request.user)
#     pests = PestDisease.objects.filter(plant_type=plant.plant_type)
#     data = [{'id': p.id, 'name': p.name} for p in pests]
#     return JsonResponse(data, safe=False)
 
# # Calculation View
# # @login_required
# # def calculate_surveillance(request):
# #     if request.method == 'POST':
# #         plant_id = request.POST.get('plant')
# #         frequency = request.POST.get('frequency')
 
# #         try:
# #             plant = Plant.objects.get(id=plant_id, grower=request.user)
# #             base_time = 2  # minutes per plant
# #             if frequency == 'weekly':
# #                 multiplier = 4
# #             elif frequency == 'monthly':
# #                 multiplier = 1
# #             else:  # daily
# #                 multiplier = 28
 
# #             total_time = plant.number_of_plants * base_time * multiplier
# #             return render(request, 'pests/surveillance_result.html', {
# #                 'plant': plant,
# #                 'total_time': total_time,
# #                 'time_period': frequency,
# #             })
# #         except Plant.DoesNotExist:
# #             messages.error(request, "Plant not found")
# #             return redirect('surveillance-create')
# #     return redirect('home')
# # About View
# class AboutView(TemplateView):
#     template_name = 'pests/about.html'