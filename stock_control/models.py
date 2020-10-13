from django.db import models
from django.core.validators import RegexValidator

# Create your models here.


class Producto(models.Model):
    categoría = models.CharField(max_length=50, blank=True, null=True)
    marca = models.CharField(max_length=50, blank=True, null=True)
    nombre = models.CharField(max_length=50, default='Producto')
    cantidad = models.IntegerField(default='0')
    código = models.CharField(primary_key=True, max_length=13, validators=[RegexValidator(r'^[1-9]^\d{1,13}$')])
    imagen = models.ImageField(blank=True, null=True)
    precio = models.DecimalField(max_digits=20, decimal_places=2, default=0)

    def __str__(self):
        return self.nombre + ": " + str(self.cantidad) + " unidades" + " $" + str(self.precio)
