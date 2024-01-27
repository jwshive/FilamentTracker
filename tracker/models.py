from django.db import models


class Printers(models.Model):
    printer_name = models.CharField(max_length=255)
    printer_make = models.CharField(max_length=255)
    printer_model = models.CharField(max_length=255)

    def __str__(self):
        return '{} [{} {}]'.format(self.printer_name, self.printer_make, self.printer_model )

    class Meta:
        verbose_name_plural = 'Printers'


class FilamentManufacturer(models.Model):
    manufacturer_name = models.CharField(max_length=255)

    def __str__(self):
        return self.manufacturer_name

    class Meta:
        verbose_name_plural = 'Filament Manufacturer'


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


class FilamentConfiguration(models.Model):
    bed_type = models.ForeignKey(PrintBeds, on_delete=models.DO_NOTHING)
    filament_brand = models.ForeignKey(FilamentManufacturer, on_delete=models.DO_NOTHING)
    printer = models.ForeignKey(Printers, on_delete=models.DO_NOTHING)
    filament_type = models.ForeignKey(FilamentTypes, on_delete=models.DO_NOTHING)
    filament_color = models.CharField(max_length=255)
    flow_rate = models.DecimalField(decimal_places=3, max_digits=5)
    pressure_advance = models.DecimalField(decimal_places=3, max_digits=5)
    first_layer_temp = models.IntegerField()
    other_layer_temp = models.IntegerField()
    plate_temp = models.IntegerField()
    max_volumetric_speed = models.DecimalField(decimal_places=3, max_digits=5)
    filament_image = models.ImageField(upload_to='filament_images')

    def __str__(self):
        return '{} {} {} on {} {} with a {}'.format(self.filament_brand.manufacturer_name, self.filament_color, self.filament_type.filament_type, self.printer.printer_make, self.printer.printer_model, self.bed_type.bed_type)

    class Meta:
        verbose_name_plural = 'Filament Configurations'
