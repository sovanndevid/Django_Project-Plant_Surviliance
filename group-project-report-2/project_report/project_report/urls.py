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
from pest_web.views import HomeView, AboutView, PestDiseaseListView
# from . import views
# , PestDiseaseDetailView register  # fixed class names
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', HomeView.as_view(), name='home'),
    re_path(r'^pests/$', PestDiseaseListView.as_view(), name='pest_list'), 
    # re_path(r'^pests/(?P<pk>\d+)/s*$', PestDiseaseDetailView.as_view(), name='pest_detail'),
    re_path(r'^about/$', AboutView.as_view(), name='about'),

    # Account
    # path('register/', views.register, name="register"),

    # # Login/Logout
    # path('login/', auth_views.LoginView.as_view(template_name='pests/login.html'), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
]
