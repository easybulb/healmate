from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.AboutPage.as_view(), name='about'),
    path('contact-us/', views.ContactPage.as_view(), name='contact_us'),
    path('join-us/', views.JoinUsPage.as_view(), name='join_us'),
    path('tools/', views.ToolsPage.as_view(), name='tools'),
    path('faq/', views.FAQPage.as_view(), name='faq'),
]
