from django import forms
from dashboard.models import PatientProfile

class PatientProfileForm(forms.ModelForm):
    class Meta:
        model = PatientProfile
        fields = ['contact_number' 'address', 'date_of_birth', 'gender', 'medical_history', 'emergency_contact']  # More fields if necessary
