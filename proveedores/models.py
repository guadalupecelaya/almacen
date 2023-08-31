from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class Proveedor(models.Model):
    nombre = models.CharField("Nombre", max_length=50, blank=False, unique=False)
    razonsocial = models.CharField(
        'Razón Social',
        max_length=60,
        null=True,
        blank=False)
    domicilio = models.CharField(
        'Domicilio',
        max_length=60,
        null=True,
        blank=False)
    telefono = models.BigIntegerField("Teléfono")
    rfc = models.CharField(
        'RFC',
        max_length=13,
        null=True,
        blank=False)
    correoelectronico = models.CharField("E-mail",max_length=50, default='', blank=False, null=True)
    regimenfiscal = models.CharField(
        'Regimen Fiscal',
        max_length=70,
        null=True,
        blank=False)
    
    #nombre = models.ForeignKey("materiales.TipoMaterial", verbose_name="Nombre", on_delete=models.CASCADE) 

    def __str__ (self):
        return self.nombre

    
