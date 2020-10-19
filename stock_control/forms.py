from django import forms
from django.forms import ModelForm, ModelMultipleChoiceField, widgets
from .models import Producto, Categoría

class ProductoForm(forms.ModelForm):
    categoría = ModelMultipleChoiceField(widget=widgets.SelectMultiple(), queryset=Categoría.objects.all())
    class Meta:
        model = Producto
        fields = ('__all__')

class CategoríaForm(forms.ModelForm):
    class Meta:
        model = Categoría
        fields = ('__all__')
