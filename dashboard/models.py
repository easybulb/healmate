from django.db import models
from django.contrib.auth.models import User

class PatientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact_number = models.CharField(max_length=15)
    address = models.CharField(max_length=255, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    gender_choices = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=gender_choices, blank=True, null=True)
    medical_history = models.TextField(blank=True, null=True)
    emergency_contact = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Patient Profile"



class Specialty(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Specialties"

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
    
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE, related_name='dashboard_appointments')
    specialist = models.ForeignKey(SpecialistProfile, on_delete=models.CASCADE, related_name='dashboard_specialist_appointments')
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Scheduled')

    def __str__(self):
        return f"Appointment with {self.specialist.user.username} on {self.date} at {self.time}"



class Message(models.Model):
    sender = models.ForeignKey(User, related_name="sent_messages", on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name="received_messages", on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.sender.username} to {self.receiver.username} on {self.timestamp}"



class Feedback(models.Model):
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE)
    specialist = models.ForeignKey(SpecialistProfile, on_delete=models.CASCADE)
    review = models.TextField()
    rating = models.PositiveIntegerField()  # Assume rating is from 1 to 5
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Feedback by {self.patient.user.username} for {self.specialist.user.username} - Rating: {self.rating}"
