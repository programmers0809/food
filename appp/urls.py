from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Home page
    path('about/', views.about, name='about'),
    path('booking/', views.booking, name='booking'),
    path('contact/', views.contact, name='contact'),
    path('menu/', views.menu, name='menu'),
    path('services/', views.services, name='services'),
    path('team/', views.team, name='team'),
    path('testimonials/', views.testimonials, name='testimonials'),
]
