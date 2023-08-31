from django.shortcuts import render, redirect
from .models import Departamento
from .forms import DepartamentoForm
from django.views.generic import ListView
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin

# Create your views here.

class DepartamentoList(PermissionRequiredMixin, ListView):
    permission_required = ['usuario.manager_permiso']
    paginate_by = 10
    model = Departamento
    context_object_name = 'departamentos'
    extra_context = {'etiqueta': 'Lista', 'mt_lista': True}

class DepartamentoCrear(PermissionRequiredMixin, CreateView):
    permission_required = ['usuario.manager_permiso']
    model = Departamento
    form_class = DepartamentoForm
    extra_context = {'etiqueta': 'Nuevo', 'boton': 'Agregar', 'dpto_nuevo': True}
    success_url = reverse_lazy('departamentos:lista')


class DepartamentoDelete( DeleteView):
    model = Departamento
    extra_context = {'etiqueta':'Eliminar', 'user_del':True}
    success_url = reverse_lazy('departamentos:lista')
