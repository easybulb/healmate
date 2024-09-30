from django.urls import path
from .views import (
    AdminDashboardView, 
    SpecialistDashboardView, 
    PatientDashboardView, 
    patient_profile, 
    request_account_deletion, 
    specialist_profile
)

urlpatterns = [
    path('admin/', AdminDashboardView.as_view(), name='admin_dashboard'),
    path('specialist/', SpecialistDashboardView.as_view(), name='specialist_dashboard'),
    path('patient/', PatientDashboardView.as_view(), name='patient_dashboard'),
    path('specialist/profile/', specialist_profile, name='specialist_profile'),
    path('profile/', patient_profile, name='patient_profile'),
    path('request-account-deletion/', request_account_deletion, name='request_account_deletion'),
    path('inbox/', views.inbox, name='inbox'),
    path('send_message/<int:user_id>/', views.send_message, name='send_message'),
]
