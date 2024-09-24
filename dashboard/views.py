from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator

# Create your views here.
# Function to check if the user is a patient
def is_patient(user):
    return user.groups.filter(name='Patient').exists()


# Function to check if the user is a specialist
def is_specialist(user):
    return user.groups.filter(name='Specialist').exists()


# Function to check if the user is an admin
def is_admin(user):
    return user.groups.filter(name='Admin').exists()




@method_decorator([login_required, user_passes_test(is_patient)], name='dispatch')
class PatientDashboardView(TemplateView):
    template_name = 'dashboard/patient_dashboard.html'

@method_decorator([login_required, user_passes_test(is_specialist)], name='dispatch')
class SpecialistDashboardView(TemplateView):
    template_name = 'dashboard/specialist_dashboard.html'

@method_decorator([login_required, user_passes_test(is_admin)], name='dispatch')
class AdminDashboardView(TemplateView):
    template_name = 'dashboard/admin_dashboard.html'