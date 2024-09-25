from django.shortcuts import render
from dashboard.models import SpecialistProfile, Specialty
from django.db.models import Q


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

    specialties = Specialty.objects.all()

    return render(request, 'specialists/search_results.html', {'specialists': specialists, 'specialties': specialties})

