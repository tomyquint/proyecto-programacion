from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import Producto, Categoría
from .forms import ProductoForm

# Create your views here.
def consulta_es_válida(parametro):
    if parametro != '' and parametro is not None:
        return True
    else:
        return False

@login_required
def lista_productos(request):
    qs = Producto.objects.all()
    categorías = Categoría.objects.all()
    nombre_contiene = request.GET.get('nombre_contiene')
    marca_contiene = request.GET.get('marca_contiene')
    categoría = request.GET.get('categoría')
    precio_mínimo = request.GET.get('precio_mínimo')
    precio_máximo = request.GET.get('precio_máximo')

    if consulta_es_válida(nombre_contiene):
        qs= qs.filter(nombre__icontains=nombre_contiene)

    if consulta_es_válida(marca_contiene):
        qs= qs.filter(marca__icontains=marca_contiene)

    if consulta_es_válida(precio_mínimo):
        qs = qs.filter(precio__gte=precio_mínimo)

    if consulta_es_válida(precio_máximo):
        qs = qs.filter(precio__lte=precio_máximo)

    if consulta_es_válida(categoría):
        qs = qs.filter(categoría__nombre=categoría)

    contexto = {
        'queryset': qs,
        'categorías': categorías,
    }

    return render(request, 'stock_control/lista_productos.html', contexto)

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
