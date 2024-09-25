from django.urls import path
from . import views

urlpatterns = [
    path('book/<int:specialist_id>/', views.book_appointment, name='book_appointment'),
    path('confirmation/', views.appointment_confirmation, name='appointment_confirmation'),
]
