from django.shortcuts import render
from .models import Producto

# Create your views here.
def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'stock_control/lista_productos.html', {'productos': productos})
