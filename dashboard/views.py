from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class PatientDashboardView(TemplateView):
    template_name = 'dashboard/patient_dashboard.html'

class SpecialistDashboardView(TemplateView):
    template_name = 'dashboard/specialist_dashboard.html'

class AdminDashboardView(TemplateView):
    template_name = 'dashboard/admin_dashboard.html'