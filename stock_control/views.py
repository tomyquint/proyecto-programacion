from django.shortcuts import render

# Create your views here.
def lista_productos(request):
    return render(request, 'stock_control/lista_productos.html', {})
