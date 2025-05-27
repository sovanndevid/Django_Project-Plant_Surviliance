
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.views import View  
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import JsonResponse
from django.db.models import Q
from django.utils import timezone
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist

from .models import PestDisease, PlantPart, Farm, SurveillanceRecord, Tree
from .forms import PestDiseaseForm, PlantPartForm, FarmForm, UserRegisterForm, SurveillanceRecordForm, TreeForm, UserProfileForm



# Displaying a list of 7 pest diseases
class PestDiseaseListView(ListView):
    model = PestDisease
    template_name = 'pests/plist.html'
    context_object_name = 'pests'
    
    def get_queryset(self):
        """Return all pest diseases ordered by name"""
        return PestDisease.objects.all().order_by('name')

# Displaying individual pest disease
class PestDiseaseDetailView(DetailView):
    """Detail view for a single pest/disease"""
    model = PestDisease
    template_name = 'pests/details.html'
    context_object_name = 'pest'
    
    
# Displaying home page at localhost/ link 
class HomeView(TemplateView):
    """Home page view"""
    template_name = 'pests/home.html'
    
    
class AboutView(TemplateView):
    """About page view"""
    template_name = 'pests/about.html'
    
    
# User register

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
    
    return render(request, 'pests/auth/register.html', {
        'user_form': user_form,
        'farm_form': farm_form
    })



# User Profile
class UserProfileView(View):
    def get(self, request):
        user_form = UserProfileForm(instance=request.user)
        farm = getattr(request.user, 'farm', None)
        farm_form = FarmForm(instance=farm)
        return render(request, 'pests/auth/user_profile.html', {
            'user_form': user_form,
            'farm_form': farm_form
        })

    def post(self, request):
        user_form = UserProfileForm(request.POST, instance=request.user)
        farm = getattr(request.user, 'farm', None)
        farm_form = FarmForm(request.POST, instance=farm)
        if user_form.is_valid() and farm_form.is_valid():
            user_form.save()
            farm = farm_form.save(commit=False)
            farm.grower = request.user
            farm.save()
            messages.success(request, "Profile and farm details updated successfully!")
            return redirect('user_profile')
        return render(request, 'pests/auth/user_profile.html', {
            'user_form': user_form,
            'farm_form': farm_form
        })
# Dashboard

class DashboardManagementView(TemplateView):
    template_name = 'pests/auth/dashboard_management.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        farm = getattr(self.request.user, 'farm', None)
        context['farm'] = farm
        if farm:
            context['num_records'] = SurveillanceRecord.objects.filter(farm=farm).count()
            context['num_trees'] = Tree.objects.filter(farm=farm).count()
            context['last_record'] = SurveillanceRecord.objects.filter(farm=farm).order_by('-created_at').first()
        else:
            context['num_records'] = 0
            context['num_trees'] = 0
            context['last_record'] = None
        return context











# Surveillance
class SurveillanceDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'pests/surveillance/surveillance_base.html' 
    # function is used to either approve or deny access to surveillance page
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return render(request, 'pests/surveillance/access_denied.html', status=403)
            
        try:
            if not hasattr(request.user, 'farm'):
                return render(request, 'pests/surveillance/access_denied.html')
        except ObjectDoesNotExist:
            messages.warning(request, "Farm profile not found.")
            return redirect('register')
        
        return super().dispatch(request, *args, **kwargs)
    
    # this function retrieves the data before executing post() function
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Get all records and trees for the current farm
        records = SurveillanceRecord.objects.filter(
            farm=self.request.user.farm,
        ).order_by('-created_at')
        
        trees = Tree.objects.filter(farm=self.request.user.farm).order_by('tag_number')
        
        # Handle edit case 
        edit_id = self.request.GET.get('edit')
        if edit_id:
            context['edit_record'] = get_object_or_404(SurveillanceRecord, pk=edit_id, farm=self.request.user.farm)
            context['form'] = SurveillanceRecordForm(
                instance=context['edit_record'],
                user=self.request.user
            )
        else:
            context['form'] = SurveillanceRecordForm(user=self.request.user)
        
        context['records'] = records
        context['trees'] = trees
        context['tree_form'] = TreeForm()  # Form for adding new trees
        return context
    
    # Function only runs when a user submits form
    def post(self, request, *args, **kwargs):
        action = request.POST.get('action')
        
        if action == 'create':
            form = SurveillanceRecordForm(request.POST, user=request.user)
            if form.is_valid():
                record = form.save(commit=False)
                record.farm = request.user.farm
                record.is_submitted = True
                record.end_time = timezone.now()
                record.save()
                messages.success(request, "Record created successfully!")
            else:
                for error in form.errors.values():
                    messages.error(request, error)
        
        elif action == 'update':
            record_id = request.POST.get('record_id')
            record = get_object_or_404(SurveillanceRecord, pk=record_id, farm=request.user.farm)
            form = SurveillanceRecordForm(request.POST, instance=record, user=request.user)
            if form.is_valid():
                form.save()
                messages.success(request, "Record updated successfully!")
            else:
                for error in form.errors.values():
                    messages.error(request, error)
        
        elif action == 'delete':
            record_id = request.POST.get('record_id')
            record = get_object_or_404(SurveillanceRecord, pk=record_id, farm=request.user.farm)
            record.delete()
            messages.success(request, "Record deleted successfully!")
            
        elif action == 'add_tree':
            tree_form = TreeForm(request.POST)
            if tree_form.is_valid():
                tree = tree_form.save(commit=False)
                tree.farm = request.user.farm
                tree.save()
                messages.success(request, "Tree added successfully!")
            else:
                for error in tree_form.errors.values():
                    messages.error(request, error)
        
        return redirect(reverse('surveillance_dashboard'))
    
class TreeDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'pests/surveillance/surveillance_base.html'  
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        trees = Tree.objects.filter(
            farm=self.request.user.farm
        ).order_by('tag_number')
        
        edit_id = self.request.GET.get('edit_tree')
        if edit_id:
            context['edit_tree'] = get_object_or_404(Tree, pk=edit_id, farm=self.request.user.farm)
            context['tree_form'] = TreeForm(
                instance=context['edit_tree']
            )
        else:
            context['tree_form'] = TreeForm()
        
        context['trees'] = trees
        return context
    
    def post(self, request, *args, **kwargs):
        action = request.POST.get('action')
        
        if action == 'create_tree':
            form = TreeForm(request.POST)
            if form.is_valid():
                tree = form.save(commit=False)
                tree.farm = request.user.farm
                tree.save()
                messages.success(request, "Tree created successfully!")
            else:
                for error in form.errors.values():
                    messages.error(request, error)
        
        elif action == 'update_tree':
            tree_id = request.POST.get('tree_id')
            tree = get_object_or_404(Tree, pk=tree_id, farm=request.user.farm)
            form = TreeForm(request.POST, instance=tree)
            if form.is_valid():
                form.save()
                messages.success(request, "Tree updated successfully!")
            else:
                for error in form.errors.values():
                    messages.error(request, error)
        
        elif action == 'delete_tree':
            tree_id = request.POST.get('tree_id')
            tree = get_object_or_404(Tree, pk=tree_id, farm=request.user.farm)
            tree.delete()
            messages.success(request, "Tree deleted successfully!")
        
        return redirect(reverse('tree_dashboard'))