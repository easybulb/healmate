from allauth.account.forms import SignupForm, LoginForm 
from django import forms
from django.contrib.auth.forms import AuthenticationForm

class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='First Name', required=True)
    last_name = forms.CharField(max_length=30, label='Last Name', required=True)
    contact_number = forms.CharField(max_length=15, label='Contact Number', required=True)
    address = forms.CharField(max_length=255, label='Address', required=True)
    date_of_birth = forms.DateField(
        label='Date of Birth', 
        required=True, 
        widget=forms.SelectDateWidget(years=range(1950, 2024))
    )
    gender = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], label='Gender', required=True)

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        # Saving the PatientProfile fields
        user.patientprofile.contact_number = self.cleaned_data.get('contact_number')
        user.patientprofile.address = self.cleaned_data.get('address')
        user.patientprofile.date_of_birth = self.cleaned_data.get('date_of_birth')
        user.patientprofile.gender = self.cleaned_data.get('gender')
        user.patientprofile.save()
        return user


# Custom authentication form to prevent login for inactive users
class CustomAuthenticationForm(LoginForm):
    def confirm_login_allowed(self, user):
        if not user.is_active:
            raise forms.ValidationError(
                "This account is inactive.",
                code='inactive',
            )
