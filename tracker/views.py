from django.shortcuts import render
from .models import FilamentConfiguration, PrinterConfiguration


def get_configurations(request):
    configs = FilamentConfiguration.objects.all().order_by('filament__manufacturer_name')
    return render(request, 'filament/filament_configuration_list.html', {'configs': configs})


def filament_config_detail(request, id):
    config = FilamentConfiguration.objects.get(id=id)
    return render(request, 'filament/filament_config_details.html', {'config': config})


def get_printers(request):
    printers = PrinterConfiguration.objects.all().order_by('printer__printer_make')
    return render(request, 'printer/printer_configuration_list.html', {'printers': printers})