from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('destination/', views.destination, name='destination'),
    path('tips/', views.tips, name='tips'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('guides/', views.guides, name='guides'),  # New guides page
]