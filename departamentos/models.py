from django.db import models

# Create your models here.
class Departamento(models.Model):
    nombre = models.CharField(
        'nombre',
        max_length=100,
        null=False,
        blank=False,
        unique=True,
        default="")
    
    def __str__ (self):
        return self.nombre
