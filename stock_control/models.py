from django.db import models

# Create your models here.
class Producto(models.Model):
    categoría = models.CharField(max_length=50, blank=True, null=True)
    marca = models.CharField(max_length=50, blank=True, null=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    cantidad = models.IntegerField(default='0', blank=True, null=True)
    código = models.BigIntegerField(max_length=13, blank=True, null=True)

    def __str__(self):
        return self.nombre + ": " + str(self.cantidad) + " unidades"
