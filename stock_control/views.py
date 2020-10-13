from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
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
    return render(request, 'stock_control/editar_producto.html', {'form': form})

@login_required
def editar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == "POST":
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            producto = form.save(commit=False)
            producto.save()
            return redirect('detalle_producto', pk=producto.pk)
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'stock_control/editar_producto.html', {'form': form})

@login_required
def signup(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('/')
    return render(request, 'registration/signup.html', {'form': form})
