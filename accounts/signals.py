from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User, Group
from dashboard.models import PatientProfile

@receiver(post_save, sender=User)
def add_to_patients_group_and_create_profile(sender, instance, created, **kwargs):
    if created:
        patients_group, _ = Group.objects.get_or_create(name='Patients')
        instance.groups.add(patients_group)
        PatientProfile.objects.get_or_create(user=instance)
        