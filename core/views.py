from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from dashboard.models import Specialty
from django.contrib import messages
from .forms import ContactForm
from .models import ContactMessage
from django.conf import settings
from django.views import View
from django.core.mail import send_mail

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
            # Save the message to the database
            ContactMessage.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                message=form.cleaned_data['message']
            )

            # Send the email
            send_mail(
                subject=f"New Contact Message from {form.cleaned_data['name']}",
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=[settings.DEFAULT_FROM_EMAIL],
            )

            messages.success(request, "Thank you for contacting us. We will get back to you soon")

            return redirect('contact_us')
        return render(request, self.template_name, {'form': form})


class JoinUsPage(TemplateView):
    template_name = 'core/join_us.html'

class ToolsPage(TemplateView):
    template_name = 'core/tools.html'

class FAQPage(TemplateView):
    template_name = 'core/faq.html'
