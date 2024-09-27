from django.contrib import admin
from .models import PatientProfile

# Register your models here.
@admin.register(PatientProfile)
class PatientProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_active')  # Shows the user and their active status
    list_filter = ('is_active',)  # Allows filtering by active/inactive status