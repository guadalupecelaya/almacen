from django.shortcuts import render, redirect
from .models import Proveedor
from .forms import ProveedorForm
from django.views.generic import ListView
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin

# Create your views here.
class ProveedorList(PermissionRequiredMixin, ListView):
    permission_required = ['usuario.manager_permiso']
    paginate_by = 10
    model = Proveedor
    context_object_name = 'proveedores'
    extra_context = {'etiqueta': 'Lista', 'mt_lista': True}

class ProveedorCrear(PermissionRequiredMixin, CreateView):
    permission_required = ['usuario.manager_permiso']
    model = Proveedor
    form_class = ProveedorForm
    extra_context = {'etiqueta': 'Nuevo', 'boton': 'Agregar', 'mt_nuevo': True}
    success_url = reverse_lazy('proveedores:lista')

class ProveedorDetalle(PermissionRequiredMixin, DetailView):
    permission_required = ['usuario.manager_permiso']
    model = Proveedor

class ProveedorActualizar(PermissionRequiredMixin, UpdateView):
    permission_required = ['usuario.manager_permiso']
    model = Proveedor
    form_class = ProveedorForm
    extra_context = {
        'etiqueta': 'Actualizar',
        'boton': 'Guardar',
        'mt_edit': True}
    success_url = reverse_lazy('proveedores:lista')

class ProveedorDelete(DeleteView):
    model = Proveedor
    extra_context = {'etiqueta': 'Eliminar', 'mt_del': True}
    success_url = reverse_lazy('proveedores:lista')