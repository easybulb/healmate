from django.shortcuts import render, get_object_or_404, redirect
from dashboard.models import SpecialistProfile
from .forms import AppointmentForm
from .models import Appointment
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now
from django.contrib import messages

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


@login_required
def patient_appointments(request):
    # Fetch all appointments for the logged-in patient
    appointments = Appointment.objects.filter(
        patient=request.user.patientprofile
    ).order_by('date', 'time')
    return render(request, 'appointments/patient_appointments.html', {
        'appointments': appointments,
        'today': now().date(),  # Pass the current date to the template
    })

@login_required
def specialist_appointments(request):
    # Fetch all appointments for the logged-in specialist
    specialist_profile = get_object_or_404(SpecialistProfile, user=request.user)
    appointments = Appointment.objects.filter(
        specialist=specialist_profile
    ).order_by('date', 'time')
    return render(request, 'appointments/specialist_appointments.html', {
        'appointments': appointments,
        'today': now().date(),  # Pass the current date to the template
    })


# Appointment Cancellation View
@login_required
def cancel_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)

    # Check if the user is either the patient or the specialist linked to the appointment
    if request.method == 'POST':
        if request.user == appointment.patient.user or request.user == appointment.specialist.user:
            appointment.status = 'Cancelled'
            appointment.save()
            messages.success(request, 'The appointment has been successfully canceled.')
        else:
            messages.error(request, 'You do not have permission to cancel this appointment.')

        # Redirect based on user type (patient or specialist)
        if request.user.groups.filter(name='Patient').exists():
            return redirect('patient_appointments')
        elif request.user.groups.filter(name='Specialist').exists():
            return redirect('specialist_appointments')

        return redirect('home')

    # Render the confirmation page if it's not a POST request
    return render(request, 'appointments/confirm_cancellation.html', {'appointment': appointment})


# Appointment Cancellation Confirmation View
@login_required
def confirm_cancel_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)

    # Check if the user is either the patient or the specialist linked to the appointment
    if request.user == appointment.patient.user or request.user == appointment.specialist.user:
        if request.method == 'POST':  # User confirmed the cancellation
            appointment.status = 'Cancelled'
            appointment.save()
            messages.success(request, 'The appointment has been successfully canceled.')
            
            # Redirect based on user type (patient or specialist)
            if request.user.groups.filter(name='Patient').exists():
                return redirect('patient_appointments')
            elif request.user.groups.filter(name='Specialist').exists():
                return redirect('specialist_appointments')
        else:  # GET request, show confirmation page
            return render(request, 'appointments/confirm_cancellation.html', {'appointment': appointment})
    else:
        messages.error(request, 'You do not have permission to cancel this appointment.')
        return redirect('home')
