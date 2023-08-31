from django import forms
from .models import Proveedor

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = '__all__'
        widgets = {
            # 'nombre':forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Nombre del Material', 'onFOcus':'validar{this}'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'razonsocial': forms.TextInput(attrs={'class': 'form-control'}),
            'domicilio': forms.TextInput(attrs={'class': 'form-control'}),
            #'domicilio': forms.Textarea(attrs={'rows':2, 'cols':20,'class': 'form-control'}),
            'telefono': forms.NumberInput(attrs={'class': 'form-control'}),
            'rfc': forms.TextInput(attrs={'class': 'form-control'}),
            'correoelectronico': forms.TextInput(attrs={'class': 'form-control'}),
            'regimenfiscal': forms.TextInput(attrs={'class': 'form-control'}),




        }