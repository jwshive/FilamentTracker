from django.contrib import admin
from .models import Printers, PrintBeds, Filaments, FilamentTypes, FilamentConfiguration


class PrintersAdmin(admin.ModelAdmin):
    list_display = ('printer_name', 'printer_make', 'printer_model')


class FilamentConfigurationAdmin(admin.ModelAdmin):
    list_display = ('printer', 'filament', 'bed_type')


class FilamentsAdmin(admin.ModelAdmin):
    list_display = ('manufacturer_name', 'filament_type', 'filament_color')


admin.site.register(Printers, PrintersAdmin)
admin.site.register(FilamentConfiguration, FilamentConfigurationAdmin)
admin.site.register(PrintBeds)
admin.site.register(Filaments)
admin.site.register(FilamentTypes)
