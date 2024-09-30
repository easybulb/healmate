from django.shortcuts import render, get_object_or_404
from dashboard.models import SpecialistProfile, Specialty
from django.db.models import Q
from django.core.paginator import Paginator
from appointments.models import Availability
from django.contrib.auth.decorators import login_required
from appointments.forms import AppointmentForm


# Create your views here.
def search_specialists(request):
    query = request.GET.get('q', '')
    specialty_filter = request.GET.get('specialty', '')
    location_filter = request.GET.get('location', '')
    
    specialists = SpecialistProfile.objects.all()

    if query:
        specialists = specialists.filter(
            Q(user__username__icontains=query) |
            Q(bio__icontains=query)
        )

    if specialty_filter:
        specialists = specialists.filter(specialty__name__icontains=specialty_filter)
    
    if location_filter:
        specialists = specialists.filter(location__icontains=location_filter)

    # Pagination: Limit to 5 specialists per page
    paginator = Paginator(specialists, 5)
    page_number = request.GET.get('page')
    specialists_page = paginator.get_page(page_number)

    specialties = Specialty.objects.all()

    return render(request, 'specialists/search_results.html', {
        'specialists': specialists_page,
        'specialties': specialties,
        'query': query,
        'specialty_filter': specialty_filter,
        'location_filter': location_filter,
        'total_results': specialists.count(),
    })


# Specialist Detail View
def specialist_detail(request, specialist_id):
    specialist = get_object_or_404(SpecialistProfile, id=specialist_id)
    availabilities = Availability.objects.filter(specialist=specialist).order_by('date', 'start_time')

    return render(request, 'specialists/specialist_detail.html', {
        'specialist': specialist,
        'availabilities': availabilities,
    })


# Book Appointment View
@login_required
def book_appointment(request, specialist_id):
    specialist = get_object_or_404(SpecialistProfile, id=specialist_id)
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.specialist = specialist
            appointment.patient = request.user.patientprofile  # Assuming a patient profile is linked to the user
            appointment.save()
            return redirect('appointment_confirmation')  # Redirect to a confirmation page
    else:
        form = AppointmentForm()
    
    return render(request, 'appointments/book_appointment.html', {
        'form': form,
        'specialist': specialist
    })
