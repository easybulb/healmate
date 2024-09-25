from django.shortcuts import render
from django.views.generic import TemplateView
from dashboard.models import Specialty

def home(request):
    specialties = Specialty.objects.all()
    return render(request, 'core/index.html', {'specialties': specialties})

class HomePage(TemplateView):
    template_name = 'core/home.html'

class AboutPage(TemplateView):
    template_name = 'core/about.html'

class ContactPage(TemplateView):
    template_name = 'core/contact_us.html'

class JoinUsPage(TemplateView):
    template_name = 'core/join_us.html'

class ToolsPage(TemplateView):
    template_name = 'core/tools.html'

class FAQPage(TemplateView):
    template_name = 'core/faq.html'
