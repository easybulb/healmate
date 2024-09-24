from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
from django.core.exceptions import PermissionDenied

# Function to check if the user is a patient
def is_patient(user):
    if not user.groups.filter(name='Patient').exists():
        print("User is not in the 'Patient' group")
        raise PermissionDenied  # Raise a 403 Forbidden error
    print("User is in the 'Patient' group")
    return True

# Function to check if the user is a specialist
def is_specialist(user):
    if not user.groups.filter(name='Specialist').exists():
        print("User is not in the 'Specialist' group")
        raise PermissionDenied
    print("User is in the 'Specialist' group")
    return True

# Function to check if the user is an admin
def is_admin(user):
    if not user.groups.filter(name='Admin').exists():
        print("User is not in the 'Admin' group")
        raise PermissionDenied
    print("User is in the 'Admin' group")
    return True

# Patient Dashboard View
@method_decorator([login_required, user_passes_test(is_patient)], name='dispatch')
class PatientDashboardView(TemplateView):
    template_name = 'dashboard/patient_dashboard.html'

# Specialist Dashboard View
@method_decorator([login_required, user_passes_test(is_specialist)], name='dispatch')
class SpecialistDashboardView(TemplateView):
    template_name = 'dashboard/specialist_dashboard.html'

# Admin Dashboard View
@method_decorator([login_required, user_passes_test(is_admin)], name='dispatch')
class AdminDashboardView(TemplateView):
    template_name = 'dashboard/admin_dashboard.html'
