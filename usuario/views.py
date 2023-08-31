from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from .models import Usuario
from .forms import UsuarioForm
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Group
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin


# Create your views here.
class NuevoUsuario(PermissionRequiredMixin, CreateView):
    permission_required = ['usuario.manager_permiso'] 
    model = Usuario
    form_class = UsuarioForm
    extra_context = {'etiqueta':'Nuevo', 'boton':'Agregar', 'nuevo_user':True}
    success_url = reverse_lazy('usuario:lista')

    def form_valid(self, form):
        user = form.save(commit=False)
        # user.is_active = 0
        # print (user)
        return super().form_valid(form)
    
class UsuariosList(PermissionRequiredMixin, ListView):
    permission_required = ['usuario.manager_permiso'] 
    model = Usuario
    context_object_name = 'usuarios'
    lista_grupos = Group.objects.all()
    extra_context={'user_lista':True,
                    'lista_grupos': lista_grupos}

class LoginUsuario(LoginView):
    template_name = 'login.html'
    form_class = AuthenticationForm

#cerrar sesion
def logout_view(request):
    logout(request)
    return redirect('usuario:login')

@login_required
@permission_required('auth.administrador_permiso', raise_exception=True)
def obtiene_usuario_grupo(request, id):
    if request.method != 'GET':
        return JsonResponse({'error':_('peticion incorrecta')},safe=False, status=403)
    id_usuario = request.GET.get('id')
    grupos = Groups.objects.filter(user_id=id_usuario)
    json=[]
    if not grupos:
        json.append({'error': _('sin grupos asignados')})
    for group in grupos:
        json.append({'id usuario':id_usuario,
        'id_grupo':grupo})
    return JsonResponse(json, safe=False)


def cambia_grupo(request, id_gpo, id_usuario):
    grupo = Group.objects.get(id=id_gpo)
    usuario= Usuario.objects.get(id=id_usuario)

    if grupo in usuario.groups.all():
        if usuario.groups.count() <= 1:
            messages.error(request, 'El usuario debe pertenecer a un grupo minimo')
        else:
            usuario.groups.remove(grupo)
            messages.success(request, 'El usuario ya no pertenece al grupo')
    else:
        usuario.groups.add(grupo)
        messages.success(request, 'El usuario se agrego al grupo')

    return redirect('usuario:lista')
