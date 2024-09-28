from django.db import models
from django.contrib.auth.models import User
from dashboard.models import SpecialistProfile, PatientProfile

# Create your models here.
class Appointment(models.Model):
    STATUS_CHOICES = [
        ('Scheduled', 'Scheduled'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]

    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE , related_name='appointment_patient')
    specialist = models.ForeignKey(SpecialistProfile, on_delete=models.CASCADE, related_name='appointment_specialist')
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Scheduled')

    def __str__(self):
        return f"Appointment with {self.specialist.user.username} on {self.date} at {self.time}"

class Availability(models.Model):
    specialist = models.ForeignKey(SpecialistProfile, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"Availability for {self.specialist.user.username} on {self.date} from {self.start_time} to {self.end_time}"

