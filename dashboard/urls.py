from django.urls import path
from .views import PatientDashboardView, SpecialistDashboardView, AdminDashboardView

urlpatterns = [
    path('patient/', PatientDashboardView.as_view(), name='patient_dashboard'),
    path('specialist/', SpecialistDashboardView.as_view(), name='specialist_dashboard'),
    path('admin/', AdminDashboardView.as_view(), name='admin_dashboard'),
]
