from django.db import models
from django.contrib.auth.models import User

class PatientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact_number = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.user.username}'s Patient Profile"

class Specialty(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class SpecialistProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialty = models.ForeignKey(Specialty, on_delete=models.SET_NULL, null=True)
    bio = models.TextField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.username} - {self.specialty.name}"

class Appointment(models.Model):
    STATUS_CHOICES = [
        ('Scheduled', 'Scheduled'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]
    
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE)
    specialist = models.ForeignKey(SpecialistProfile, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Scheduled')

    def __str__(self):
        return f"Appointment with {self.specialist.user.username} on {self.date} at {self.time}"

