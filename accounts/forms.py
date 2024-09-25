from allauth.account.forms import SignupForm
from django import forms

class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='First Name', required=True)
    last_name = forms.CharField(max_length=30, label='Last Name', required=True)
    contact_number = forms.CharField(max_length=15, label='Contact Number', required=True)
    address = forms.CharField(max_length=255, label='Address', required=True)
    date_of_birth = forms.DateField(label='Date of Birth', required=True, widget=forms.SelectDateWidget(years=range(1900, 2024)))
    gender = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], label='Gender', required=True)

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        user.patientprofile.contact_number = self.cleaned_data.get('contact_number')
        user.patientprofile.address = self.cleaned_data.get('address')
        user.patientprofile.date_of_birth = self.cleaned_data.get('date_of_birth')
        user.patientprofile.gender = self.cleaned_data.get('gender')
        user.patientprofile.save()
        return user
