from django.shortcuts import render
from django.views.generic import TemplateView
from dashboard.models import Specialty
from django.contrib.auth.models import Group
from django.contrib import messages
from .forms import ContactForm
from .models import ContactMessage
from django.views import View

def home(request):
    specialties = Specialty.objects.all()
    return render(request, 'core/index.html', {'specialties': specialties})

class HomePage(TemplateView):
    template_name = 'core/home.html'

class AboutPage(TemplateView):
    template_name = 'core/about.html'

class ContactPage(TemplateView):
    template_name = 'core/contact_us.html'

    def get(self, request):
        form = ContactForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent successfully.")
            return redirect('contact_us')  # Redirect to avoid resubmission on page refresh
        return render(request, self.template_name, {'form': form})

class JoinUsPage(TemplateView):
    template_name = 'core/join_us.html'

class ToolsPage(TemplateView):
    template_name = 'core/tools.html'

class FAQPage(TemplateView):
    template_name = 'core/faq.html'
