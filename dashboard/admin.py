from django.contrib import admin
from .models import PatientProfile, SpecialistProfile, Appointment, Message, Feedback, Specialty

# Register your models here.
admin.site.register(PatientProfile)
admin.site.register(SpecialistProfile)
admin.site.register(Appointment)
admin.site.register(Message)
admin.site.register(Feedback)
admin.site.register(Specialty)