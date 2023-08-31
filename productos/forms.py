from django import forms
from .models import Producto, TipoProducto

class TipoProductoForm(forms.ModelForm):
    class Meta:
        model = TipoProducto
        fields  = ('nombre',)

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
        widgets = {
            # 'nombre':forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Nombre del Material', 'onFOcus':'validar{this}'}),
            'nombre': forms.Select(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
            'fecha': forms.DateField(),
            'proveedor':forms.Select(attrs={'class': 'form-control'}),

        }