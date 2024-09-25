from django import forms
from dashboard.models import PatientProfile

class PatientProfileForm(forms.ModelForm):
    class Meta:
        model = PatientProfile
        fields = ['contact_number']  # More fields if necessary
