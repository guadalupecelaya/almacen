from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, TipoProducto
from .forms import ProductoForm, TipoProductoForm
from django.views.generic import ListView
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.
@login_required
@permission_required('usuario.manager_permiso', raise_exception=True)
def lista_tipoproducto(request):
    tipoproductos = TipoProducto.objects.all()
    context = {'tipoproductos': tipoproductos, "cat_lista":True}
    return render(request, 'tipoproducto_list.html', context)

@login_required
@permission_required('usuario.manager_permiso', raise_exception=True)
def nuevo_tipoproducto(request):
    form = TipoProductoForm()
    if request.method == 'POST':
        form = TipoProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tipoproducto:lista')

    context = {'form' : form, "tmt_nueva":True}
    return render(request, 'tipoproducto_form.html', context)

def eliminar_tipoproducto(request, id):
    tipoproducto = get_object_or_404(TipoProducto, id=id)
    tipoproducto.delete()
    
    return redirect('tipoproducto:lista')

@login_required
@permission_required('usuario.manager_permiso', raise_exception=True)
def editar_tipoproducto(request, id):
    tipoproducto = get_object_or_404(TipoProducto, id=id)
    form = TipoProductoForm(instance=tipoproducto)
    if request.method == 'POST':
        form = TipoProductoForm(request.POST, instance=tipoproducto)
        if form.is_valid():
            form.save()
            return redirect('tipoproducto:lista')
    context = {'form' : form, "cat_edit":True}
    return render(request, 'editar_tipoproducto.html', context)  

class ProductoList(PermissionRequiredMixin, ListView):
    permission_required = ['usuario.manager_permiso']
    paginate_by = 10
    model = Producto
    context_object_name = 'productos'
    extra_context = {'etiqueta': 'Lista', 'mt_lista': True}

class ProductoCrear(PermissionRequiredMixin, CreateView):
    model = Producto
    form_class = ProductoForm
    extra_context = {'etiqueta': 'Nuevo', 'boton': 'Agregar', 'mt_nuevo': True}
    success_url = reverse_lazy('productos:lista')

@login_required
@permission_required('usuario.manager_permiso', raise_exception=True)
def nuevo_producto(request):
    form = ProductoForm()
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            tipoproducto = TipoProducto.objects.get(id = request.POST['nombre'])
            cantidad= form.cleaned_data.get("cantidad")
            tipoproducto.cantidad += cantidad
            form.save()
            tipoproducto.save()
            return redirect('productos:lista')

    context = {'form' : form}
    return render(request, 'productos/producto_form.html', context)


class ProductoActualizar(PermissionRequiredMixin, UpdateView):
    permission_required = ['usuario.manager_permiso']
    model = Producto
    form_class = ProductoForm
    extra_context = {
        'etiqueta': 'Actualizar',
        'boton': 'Guardar',
        'mt_edit': True}
    success_url = reverse_lazy('productos:lista')

class ProductoDelete(DeleteView):
    model = Producto
    extra_context = {'etiqueta': 'Eliminar', 'mt_del': True}
    success_url = reverse_lazy('productos:lista')
