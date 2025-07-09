from django.urls import path
from . import views

urlpatterns = [
    path('', views.analog_clock, name='analog_clock'),
]