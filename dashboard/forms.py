from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
from dashboard.models import PatientProfile
from dashboard.models import SpecialistProfile

class SpecialistProfileForm(forms.ModelForm):
    class Meta:
        model = SpecialistProfile
        fields = ['specialty', 'bio', 'location', 'profile_image']

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

# Custom authentication form to prevent login for inactive users
class CustomAuthenticationForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        if not user.is_active:
            raise forms.ValidationError(
                "This account is inactive.",
                code='inactive',
            )