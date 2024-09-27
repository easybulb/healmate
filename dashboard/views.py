from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
from django.contrib import messages
from dashboard.models import PatientProfile, SpecialistProfile
from dashboard.forms import SpecialistProfileForm
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Fetch only active profiles
        profile = PatientProfile.objects.get(user=self.request.user, is_active=True)
        if profile:
            patient_id = profile.id + 24578  # Generate the patient ID dynamically
            context['profile'] = profile
            context['patient_id'] = patient_id
        return context

# Specialist Dashboard View
@method_decorator([login_required, user_passes_test(is_specialist)], name='dispatch')
class SpecialistDashboardView(TemplateView):
    template_name = 'dashboard/specialist_dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Fetch the specialist's profile and pass it to the context
        profile = SpecialistProfile.objects.get(user=self.request.user)
        context['profile'] = profile
        return context

# Admin Dashboard View
@method_decorator([login_required, user_passes_test(is_admin)], name='dispatch')
class AdminDashboardView(TemplateView):
    template_name = 'dashboard/admin_dashboard.html'


# Specialist Profile View
@login_required
def specialist_profile(request):
    profile, created = SpecialistProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = SpecialistProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your specialist profile has been updated successfully!')
            return redirect('specialist_profile')  # Redirect after saving
    else:
        form = SpecialistProfileForm(instance=profile)

    return render(request, 'dashboard/specialist_profile.html', {
        'form': form,
        'profile': profile
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

@login_required
def request_account_deletion(request):
    profile = PatientProfile.objects.filter(user=request.user).first()

    if request.method == 'POST':
        if profile:
            profile.is_active = False  # Soft delete by deactivating the profile
            profile.save()
            messages.success(request, 'Your account has been deactivated. An admin will review your request. You can log out now.')
            logout(request)
            return redirect('home')  # Redirect to the home page after deactivation

    return render(request, 'dashboard/request_account_deletion.html')

