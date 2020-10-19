from django import forms

from .models import Producto, Categoría

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('__all__')

class CategoríaForm(forms.ModelForm):
    class Meta:
        model = Categoría
        fields = ('__all__')
