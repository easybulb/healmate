from django.urls import path
from .views import AdminDashboardView, SpecialistDashboardView, PatientDashboardView

urlpatterns = [
    path('admin/', AdminDashboardView.as_view(), name='admin_dashboard'),
    path('specialist/', SpecialistDashboardView.as_view(), name='specialist_dashboard'),
    path('patient/', PatientDashboardView.as_view(), name='patient_dashboard'),
]
