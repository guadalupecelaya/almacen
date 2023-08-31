import datetime
from django.db import models
from django.core.validators import MinValueValidator
from django.utils.timezone import now


# Create your models here
class Solicitud(models.Model):
    fechota = models.DateTimeField(default=now, editable=False, blank=False)
    producto = models.ForeignKey(
        "productos.TipoProducto",
        verbose_name="Producto",
        blank=False,
        on_delete=models.CASCADE)
    fecha = models.CharField(
        'fecha', 
        max_length=50, 
        unique=False)
    unidades = models.IntegerField(
        'Cantidad', default=1, blank=False, validators=[
            MinValueValidator(1)])
    usuario = models.ForeignKey(
        "usuario.Usuario",
        verbose_name="Usuario",
        blank=False,
        on_delete=models.CASCADE)
    departamento = models.ForeignKey(
        "departamentos.Departamento",
        verbose_name="Departamento",
        blank=False,
        on_delete=models.CASCADE)
    
    ESTADO_CHOICES = [
        ('Pendiente', 'Pendiente'),
        ('Aceptado', 'Aceptado'),
    ]
    estado = models.CharField(
        "Estado",
        max_length=20,
        blank=False,
        choices=ESTADO_CHOICES,
        default='Pendiente'
    )

    def __str__(self):
        return str(self.fechota)


    

    
 


