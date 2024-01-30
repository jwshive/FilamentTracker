from django.db import models


class Printers(models.Model):
    printer_name = models.CharField(max_length=255)
    printer_make = models.CharField(max_length=255)
    printer_model = models.CharField(max_length=255)

    def __str__(self):
        return '{} [{} {}]'.format(self.printer_name, self.printer_make, self.printer_model)

    def get_printer_full_model(self):
        return '{} {}'.format(self.printer_make, self.printer_model)

    class Meta:
        verbose_name_plural = 'Printers'


class PrintBeds(models.Model):
    bed_type = models.CharField(max_length=255)

    def __str__(self):
        return self.bed_type

    class Meta:
        verbose_name_plural = 'Bed Types'


class FilamentTypes(models.Model):
    filament_type = models.CharField(max_length=255)

    def __str__(self):
        return self.filament_type

    class Meta:
        verbose_name_plural = 'Filament Types'


class Filaments(models.Model):
    manufacturer_name = models.CharField(max_length=255, unique=True)
    filament_type = models.ForeignKey(FilamentTypes, on_delete=models.DO_NOTHING)
    filament_color = models.CharField(max_length=255)
    filament_image = models.ImageField(upload_to='filament_images')

    def __str__(self):
        return '{} {} {}'.format(self.manufacturer_name, self.filament_type, self.filament_color)

    class Meta:
        verbose_name_plural = 'Filaments'
        unique_together = ('manufacturer_name', 'filament_type', 'filament_color')


class FilamentConfiguration(models.Model):
    bed_type = models.ForeignKey(PrintBeds, on_delete=models.DO_NOTHING)
    filament = models.ForeignKey(Filaments, on_delete=models.DO_NOTHING)
    printer = models.ForeignKey(Printers, on_delete=models.DO_NOTHING)
    flow_rate = models.DecimalField(decimal_places=3, max_digits=5)
    pressure_advance = models.DecimalField(decimal_places=3, max_digits=5)
    first_layer_temp = models.IntegerField()
    other_layer_temp = models.IntegerField()
    plate_temp = models.IntegerField()
    max_volumetric_speed = models.DecimalField(decimal_places=3, max_digits=5)

    def __str__(self):
        return '{} {} {} on {} {} with a {}'.format(self.filament.manufacturer_name, self.filament.filament_color, self.filament.filament_type.filament_type, self.printer.printer_make, self.printer.printer_model, self.bed_type.bed_type)

    class Meta:
        verbose_name_plural = 'Filament Configurations'
