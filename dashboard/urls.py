from django.urls import path
from . import views

urlpatterns = [
    path('patient/', views.PatientDashboardView.as_view(), name='patient_dashboard'),
    path('specialist/', views.SpecialistDashboardView.as_view(), name='specialist_dashboard'),
    path('admin/', views.AdminDashboardView.as_view(), name='admin_dashboard'),
]
