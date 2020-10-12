from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import Producto
from .forms import ProductoForm

# Create your views here.
@login_required
def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'stock_control/lista_productos.html', {'productos': productos})

@login_required
def detalle_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, 'stock_control/detalle_producto.html', {'producto': producto})

@login_required
def producto_nuevo(request):
    if request.method == "POST":
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            archivo_imagen = Producto(imagen = request.FILES['imagen'])
            producto = form.save()
            return redirect('detalle_producto', pk=producto.pk)
    else:
        form = ProductoForm()
    return render(request, 'stock_control/producto_nuevo.html', {'form': form})
