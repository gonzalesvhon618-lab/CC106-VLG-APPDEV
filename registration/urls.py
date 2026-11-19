
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Registration, name='registration'),
    path('success/', views.RegistrationSuccess, name='registration_success'),
]
