from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class Producto(models.Model):
    #nombre = models.CharField("Nombre", max_length=30, unique=False)
    nombre = models.ForeignKey(
        "productos.TipoProducto",
        verbose_name="Nombre",
        null=True,
        blank=False,
        on_delete=models.SET_NULL)
    precio = models.DecimalField(
        'Precio',
        blank=False,
        max_digits=6,
        decimal_places=2,
        validators=[
            MinValueValidator(0)])
    cantidad = models.PositiveIntegerField('Cantidad', default=1)
    
    fecha = models.DateTimeField(auto_now_add=True)
    proveedor=models.ForeignKey(
        "proveedores.Proveedor",
        verbose_name="Proveedor",
        null=True,
        blank=False,
        on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.nombre)

    #def get_precio_total(self):
    #s    return cantidad * precio


class TipoProducto(models.Model):
    nombre = models.CharField(max_length=50, blank=False)
    cantidad = models.IntegerField('Cantidad', default=0, blank=False)


    def __str__(self):
        return self.nombre
