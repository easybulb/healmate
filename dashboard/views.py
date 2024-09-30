from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
from django.contrib import messages
from dashboard.models import PatientProfile, SpecialistProfile
from appointments.models import Appointment
from dashboard.forms import SpecialistProfileForm, PatientProfileForm
from django.contrib.auth import logout
from django.utils.timezone import now
from appointments.models import Availability
from appointments.forms import AvailabilityForm
from django.contrib.auth.models import User


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
        profile, created = PatientProfile.objects.get_or_create(user=self.request.user)
        patient_id = profile.id + 24578  # Generate the patient ID dynamically
        context['profile'] = profile
        context['patient_id'] = patient_id
        # Fetch upcoming appointments for the patient
        context['upcoming_appointments'] = Appointment.objects.filter(
            patient=profile,
            date__gte=now()
        ).order_by('date', 'time')[:3]  # Limit to next 3 upcoming appointments
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
        # Fetch upcoming appointments for the specialist
        context['upcoming_appointments'] = Appointment.objects.filter(
            specialist=profile,
            date__gte=now()
        ).order_by('date', 'time')[:3]  # Limit to next 3 upcoming appointments
        # Initialize AvailabilityForm
        form = AvailabilityForm()
        context['availability_form'] = form
        # Fetch the specialist's availability and pass it to the context
        context['availabilities'] = Availability.objects.filter(specialist=profile)

        return context

    # Handle POST request for availability form
    def post(self, request, *args, **kwargs):
        profile = SpecialistProfile.objects.get(user=self.request.user)
        form = AvailabilityForm(request.POST)
        if form.is_valid():
            availability = form.save(commit=False)
            availability.specialist = profile
            availability.save()
            messages.success(request, 'Availability successfully set!')
        else:
            messages.error(request, 'Error setting availability. Please check the form.')

        return redirect('specialist_dashboard')  # Redirect back to dashboard after saving

        

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
            request.user.is_active = False
            request.user.save()
            messages.success(request, 'Your account has been deactivated. An admin will review your request. You can log out now.')
            logout(request)
            return redirect('home')  # Redirect to the home page after deactivation

    return render(request, 'dashboard/request_account_deletion.html')


# Views for messages
# Inbox View
@login_required
def inbox(request):
    # Get all messages where the current user is the receiver
    received_messages = Message.objects.filter(receiver=request.user).order_by('-timestamp')
    return render(request, 'dashboard/inbox.html', {'received_messages': received_messages})
