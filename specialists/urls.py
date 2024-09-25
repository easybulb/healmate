from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search_specialists, name='search_specialists'),
]
