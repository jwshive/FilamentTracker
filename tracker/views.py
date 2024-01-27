from django.shortcuts import render
from django.views.generic import ListView
from .models import FilamentConfiguration


class FilamentConfigurations(ListView):
    model = FilamentConfiguration
