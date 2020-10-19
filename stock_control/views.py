from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import login, authenticate, REDIRECT_FIELD_NAME, get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Producto, Categoría
from .forms import ProductoForm, CategoríaForm

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
    código = request.GET.get('código')

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

    if consulta_es_válida(código):
        qs = qs.filter(código=código)

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
            archivo_imagen = Producto(imagen = request.FILES.get('filepath', False))
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
            producto.categoría.set(form.cleaned_data.get("categoría"))
            form.save_m2m()
            return redirect('detalle_producto', pk=producto.pk)
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'stock_control/editar_producto.html', {'form': form})

@login_required
def borrar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == "POST":
        producto.delete()
        return redirect('lista_productos')
    return render(request, 'stock_control/borrar_producto.html', {'producto': producto})

@login_required
def registro_completo(request):
    return render(request, 'registration/registro_completo.html')

@login_required
def login_superuser(request):
    form = AuthenticationForm(request.POST)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        login(request, user)
    return render(request, "registration/login_superuser.html", {'form': form})


@user_passes_test(lambda u: u.is_superuser, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login_superuser')
def signup(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('registro_completo')
    return render(request, 'registration/signup.html', {'form': form})

@user_passes_test(lambda u: u.is_superuser, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login_superuser')
def lista_usuarios(request):
    usuarios= get_user_model().objects.all()
    return render(request, 'stock_control/lista_usuarios.html', {'usuarios': usuarios})

@user_passes_test(lambda u: u.is_superuser, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login_superuser')
def borrar_usuario(request, username):
    usuario = get_user_model().objects.get(username = username)
    if request.method == "POST":
        usuario.delete()
        return redirect('lista_usuarios')
    return render(request, 'registration/borrar_usuario.html', {'usuario': usuario})

@login_required
def lista_categorías(request):
    categorías= Categoría.objects.all()
    return render(request, 'stock_control/lista_categorías.html', {'categorías': categorías})

@login_required
def categoría_nueva(request):
    if request.method == "POST":
        form = CategoríaForm(request.POST)
        if form.is_valid():
            categoría = form.save()
            return redirect(lista_categorías)
    else:
        form = CategoríaForm()
    return render(request, 'stock_control/categoría_nueva.html', {'form': form})

@login_required
def borrar_categoría(request, pk):
    categoría = get_object_or_404(Categoría, pk=pk)
    if request.method == "POST":
        categoría.delete()
        return redirect('lista_categorías')
    return render(request, 'stock_control/borrar_categoría.html', {'categoría': categoría})
