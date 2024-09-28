from django.shortcuts import render, get_object_or_404, redirect
from dashboard.models import SpecialistProfile
from .forms import AppointmentForm
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now

# Create your views here.

# Book appointment view
def book_appointment(request, specialist_id):
    specialist = get_object_or_404(SpecialistProfile, id=specialist_id)
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.specialist = specialist
            appointment.patient = request.user.patientprofile  # Ensure the user is a patient
            appointment.status = 'Scheduled'  # Set the default status to 'Scheduled'
            appointment.save()
            return redirect('appointment_confirmation')
    else:
        form = AppointmentForm()
    return render(request, 'appointments/book_appointment.html', {'form': form, 'specialist': specialist})

# Confirmation view
def appointment_confirmation(request):
    return render(request, 'appointments/appointment_confirmation.html')


