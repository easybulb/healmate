from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search_specialists, name='search_specialists'),
    path('detail/<int:specialist_id>/', views.specialist_detail, name='specialist_detail'),
    path('book/<int:specialist_id>/', views.book_appointment, name='book_appointment'), 
]
