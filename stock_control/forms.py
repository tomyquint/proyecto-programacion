from django import forms
from .models import Producto

class MostrarProductoAdmin(forms.ModelForm):
   class Meta:
     model = Producto
     fields = ['category', 'item_name', 'quantity']
