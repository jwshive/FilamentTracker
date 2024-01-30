from django.shortcuts import render
from .models import FilamentConfiguration


def get_configurations(request):
    configs = FilamentConfiguration.objects.all().order_by('filament__manufacturer_name')
    return render(request, 'tracker/configuration_list.html', {'configs': configs})


def filament_config_detail(request, id):
    config = FilamentConfiguration.objects.get(id=id)
    return render(request, 'tracker/config_details.html', {'config': config})
