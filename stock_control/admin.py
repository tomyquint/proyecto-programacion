from django.contrib import admin

# Register your models here.
from .models import Categoría, Producto

admin.site.register(Categoría)
admin.site.register(Producto)
