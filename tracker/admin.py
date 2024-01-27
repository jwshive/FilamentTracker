from django.contrib import admin
from .models import Printers, PrintBeds, FilamentManufacturer, FilamentTypes, FilamentConfiguration

admin.site.register(Printers)
admin.site.register(PrintBeds)
admin.site.register(FilamentConfiguration)
admin.site.register(FilamentManufacturer)
admin.site.register(FilamentTypes)
