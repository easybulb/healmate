from django.contrib import admin
from .models import PatientProfile, SpecialistProfile, Appointment, Message, Feedback, Specialty

# Register your models here.
@admin.register(PatientProfile)
class PatientProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_active')
    list_filter = ('is_active',)

@admin.register(SpecialistProfile)
class SpecialistProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'specialty')

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient', 'specialist', 'date', 'time', 'status')

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'timestamp')

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('patient', 'specialist', 'rating', 'date')

@admin.register(Specialty)
class SpecialtyAdmin(admin.ModelAdmin):
    list_display = ('name',)
