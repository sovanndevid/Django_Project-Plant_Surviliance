from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .pests_data import get_pests_list
from django.http import Http404


class HomeView(TemplateView):
    """Home page view"""
    template_name = 'pests/home.html'

class PestListView(ListView):
    """List of all pests"""
    template_name = 'pests/plist.html'
    context_object_name = 'pests'  # This is the variable name used in template
    
    def get_queryset(self):
        """Return the list of pests to display"""
        return get_pests_list()

class PestDetailView(DetailView):
    """Detail view for a single pest"""
    template_name = 'pests/details.html'
    context_object_name = 'pest'  # This is the variable name used in template
    
    # get_object() get the single object that the view will display
    # queryset is None as we are not working with models, so default to get_queryset()
    def get_object(self, queryset=None):
        # Get the pest ID from the URL parameter
        pest_id = self.kwargs.get('pk')
        
        # If not found, 'pest' will be None
        pest = next((p for p in get_pests_list() if p.id == pest_id), None)
        
        # If the pest doesn't exist, gracefully raise a 404 error to handle invalid URLs
        if not pest:
            raise Http404("Pest not found")
        return pest

class AboutView(TemplateView):
    """About page view"""
    template_name = 'pests/about.html'
    
def register(request):
    return render(request, 'pests/account.html') 