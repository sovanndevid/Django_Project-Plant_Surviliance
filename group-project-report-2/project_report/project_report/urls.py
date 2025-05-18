"""
URL configuration for project_report project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

""" focusing on CBV """

from django.contrib import admin
from django.urls import re_path, path
# Adding .views because it sits in app folder
from pest_web import views
from pest_web.views import HomeView, PestListView, PestDetailView, AboutView, register # built-in django classes


urlpatterns = [
    # Home View (empty path) 
    path('admin/', admin.site.urls),
    re_path(r'^$', HomeView.as_view(), name='home'),
    
    # Pest list view: ^pests/$ to match /pests/  
    re_path(r'^pests/$', PestListView.as_view(), name='pest_list'), 
    
    # Pest detail view
    # (?P<pk\d+) == <int:pest-id>  // matches one or more digit, also primary key is mapped to pest_id
    re_path(r'^pests/(?P<pk>\d+)/s*$', PestDetailView.as_view(), name='pest_detail'),

    # About view
    re_path(r'^about/$', AboutView.as_view(), name='about'),
    
    
    # account
    path('account/', views.register, name="register"),
    
]


