from django import forms
from dashboard.models import PatientProfile
from dashboard.models import SpecialistProfile

class SpecialistProfileForm(forms.ModelForm):
    class Meta:
        model = SpecialistProfile
        fields = ['specialty', 'bio', 'location']

class PatientProfileForm(forms.ModelForm):
    class Meta:
        model = PatientProfile
        fields = [
            'contact_number', 
            'address', 
            'date_of_birth', 
            'gender', 
            'medical_history', 
            'emergency_contact'
        ]