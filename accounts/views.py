from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

class HomePage(TemplateView):
    """
    Displays the homepage
    """
    template_name = 'index.html'