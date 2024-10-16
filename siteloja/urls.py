from django.urls import path
from .views import cadcli

urlpatterns = [
    path('',cadcli, name='formcli'),
]