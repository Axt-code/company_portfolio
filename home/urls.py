from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('about/', views.about, name = 'about'),
    
    path('product/<int:id>/', views.product, name = 'product'),
    path('enquiry/', views.enquiry, name = 'enquiry'),
    path('contact/', views.contact, name = 'contact'),
    path('privacy/', views.privacy, name = 'privacy'),
]
