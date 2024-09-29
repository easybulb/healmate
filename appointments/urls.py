from django.urls import path
from . import views

urlpatterns = [
    path('book/<int:specialist_id>/', views.book_appointment, name='book_appointment'),
    path('confirmation/', views.appointment_confirmation, name='appointment_confirmation'),
    path('patient/', views.patient_appointments, name='patient_appointments'),
    path('specialist/', views.specialist_appointments, name='specialist_appointments'),
    path('cancel/<int:appointment_id>/', views.cancel_appointment, name='cancel_appointment'),
    path('cancel/confirm/<int:appointment_id>/', views.confirm_cancel_appointment, name='confirm_cancel_appointment'),
]
