from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
from django.contrib import messages
from dashboard.models import PatientProfile
from dashboard.forms import PatientProfileForm

# Function to check if the user is a patient
def is_patient(user):
    return user.groups.filter(name='Patient').exists()

# Function to check if the user is a specialist
def is_specialist(user):
    return user.groups.filter(name='Specialist').exists()

# Function to check if the user is an admin
def is_admin(user):
    return user.groups.filter(name='Admin').exists()

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


@login_required
def patient_dashboard(request):
    profile = PatientProfile.objects.get(user=request.user)
    patient_id = profile.id + 24578  # Generate patient ID dynamically
    return render(request, 'dashboard/patient_dashboard.html', {
        'profile': profile,
        'patient_id': patient_id  # Pass the generated patient ID to the template
    })



# Patient Profile View
@login_required
def patient_profile(request):
    profile, created = PatientProfile.objects.get_or_create(user=request.user)
    patient_id = profile.id + 24578  # Generates patient ID dynamically

    if request.method == 'POST':
        form = PatientProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully!')
            return redirect('patient_profile')  # Redirect to the profile page after saving
    else:
        form = PatientProfileForm(instance=profile)

    return render(request, 'dashboard/patient_profile.html', {
        'form': form,
        'profile': profile,
        'patient_id': patient_id # Pass the generated patient ID to the template
    })
