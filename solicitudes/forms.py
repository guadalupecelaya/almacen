from django import forms
from .models import Solicitud

class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitud
        fields = ('producto', 'fecha', 'unidades', 'departamento')
        widgets = {
            # 'nombre':forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Nombre del Material', 'onFOcus':'validar{this}'}),
            'producto': forms.Select(attrs={'class': 'form-control'}),
            'fecha': forms.DateInput(format='%d/%m/%Y'),
            'unidades': forms.NumberInput(attrs={'class': 'form-control'}),
            'departamento': forms.Select(attrs={'class': 'form-control'}),

        }

      
