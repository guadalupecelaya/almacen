
from .models import Solicitud
from .forms import SolicitudForm
from django.views.generic import ListView
from django.views.generic.edit import  CreateView, UpdateView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from usuario.models import Usuario
from productos.models import Producto, TipoProducto
from departamentos.models import Departamento
from django.shortcuts import render, redirect
import datetime

# Create your views here.
class SolicitudList(ListView):
    model = Solicitud
    context_object_name = 'solicitudes'
    extra_context = {'etiqueta': 'Lista', 'mt_lista': True}

class SolicitudCrear(CreateView):
    model = Solicitud
    form_class = SolicitudForm
    extra_context = {'etiqueta': 'Nuevo', 'boton': 'Agregar', 'mt_nuevo': True}
    success_url = reverse_lazy('solicitudes:lista')

def solicitud_nueva(request):
    form = SolicitudForm()
    if request.method == 'POST':
        try:
            form = SolicitudForm(request.POST, request.FILES)
            if form.is_valid():
                fecha = form.cleaned_data.get("fecha")
                unidades= form.cleaned_data.get("unidades")                
                producto = TipoProducto.objects.get(id = request.POST['producto'])
                departamento = Departamento.objects.get(id = request.POST['departamento'])
                usuario = Usuario.objects.get(username = request.user.username)

                sol = Solicitud.objects.create(producto=producto,
                                            fecha = fecha,
                                            unidades = unidades,
                                            usuario = usuario,
                                            departamento=departamento)
                
                #tipoproducto = TipoProducto.objects.get(id = request.POST['producto'])
                #cantidad= form.cleaned_data.get("unidades")
                #tipoproducto.cantidad -= cantidad
                #tipoproducto.save()

                result = sol.save()
                context = {'form':form, 'status': "ok", 'mensaje':"Solicitud realizada."}
                return redirect('solicitudes:lista')
                
        except:
            print("NO FUNCIONA")
            context = {'form':form, 'status': "error", 'mensaje':"Datos incorrectos."}
            return render(request, 'solicitudes/solicitud_form.html', context)
    context = {'form':form, 'status': "nuevo"}
    return render(request, 'solicitudes/solicitud_form.html', context)

def aceptar_solicitud(request, id):
    solicitud=Solicitud.objects.get(id=id)
    unidades= solicitud.unidades
    tipo = solicitud.producto
    tipoproducto = TipoProducto.objects.get(nombre=tipo)
    cantidad = tipoproducto.cantidad
    tipoproducto.cantidad -= unidades
    solicitud.estado = 'Aceptado'
    tipoproducto.save()
    solicitud.save()

    return redirect('solicitudes:lista')




    
   